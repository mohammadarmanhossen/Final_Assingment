from rest_framework import serializers
from .models import District
from .import models

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'district_name', 'slug']


class HotelSerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='district_names.district_name', read_only=True)

    class Meta:
        model = models.Hotel
        fields = [
            'id', 
            'hotel_name', 
            'address', 
            'district_name',  # Fetches the name of the related district
            'image', 
            'description', 
            'price_per_night', 
            'available_room'
        ]



class ReviewSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='hotel.name', read_only=True)
    class Meta:
        model = models.Review
        fields = ['id', 'rating', 'user', 'created', 'body', 'hotel_name']

class BookedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booked
        fields = '__all__' 