from rest_framework import serializers
from projeto_clima.models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'name', 'state', 'country', 'meteogram']