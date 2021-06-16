from rest_framework import serializers
from .models import Cars, Rent

class CarsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Cars
class RentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Rent