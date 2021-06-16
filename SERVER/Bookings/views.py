from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .forms import BookingDetailsForm
from .models import Rent, Cars
from .serializer import CarsSerializer, RentSerializer


# Create your views here.
class CarsList(generics.ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class CarsDetail(generics.RetrieveAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class RentList(generics.ListAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
class RentListCreateApiView(ListCreateAPIView):
    serializer_class = RentSerializer
    queryset = Rent.objects.all()
@csrf_exempt
def check_booking_details(request):
    form = BookingDetailsForm()
    return render(request,'booking/home.html', {'form': form})


@csrf_exempt
@api_view(['GET','POST'])
def create_booking(request):
    if request.method == 'POST':
        booking_data = JSONParser().parse(request)
        booking_serializer = RentSerializer(data=booking_data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            return JsonResponse(booking_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def book(request):
    if request.method == 'POST':
        # data = Request.data
        data = JSONParser().parse(request)
        print(data)
        booking = Rent.objects.get_or_create(first_name=data['first_name'], second_name=data['last_name'],
                                      telephone=data['phone_number'], from_date=data['from_date'],
                                      to_date=data['to_date'])
        # booking_data = Rent(first_name=data['first_name'])
        booking.save()
    return HttpResponse("Booking Successful!!!")
