from django.urls import path
from . import views

urlpatterns = [
    path('',views.CarsList.as_view()),
    path('<int:pk>/', views.CarsDetail.as_view(), name='booking'),
    path('rented/', views.RentList.as_view(),name='Rented_list'),
    path('book/', views.RentListCreateApiView.as_view(), name='api-post-book'),
    path('bookdetails/', views.check_booking_details, name='bookdetails')
]