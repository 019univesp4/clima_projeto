from rest_framework import serializers
from projeto_clima.models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = [
            'id', 'weather', 'date', 'date_br',
            'humidity_min', 'humidity_max',
            'humidity_dawn_min', 'humidity_dawn_max',
            'humidity_morning_min', 'humidity_morning_max',
            'humidity_afternoon_min', 'humidity_afternoon_max',
            'humidity_night_min', 'humidity_night_max',
            'pressure', 'rain_precipitation', 'rain_probability',
            'wind_velocity_min', 'wind_velocity_max', 'wind_velocity_avg',
            'wind_direction', 'wind_gust_max', 'uv_max',
            'thermal_sensation_min', 'thermal_sensation_max',
            'temperature_min', 'temperature_max',
            'temperature_dawn_min', 'temperature_dawn_max',
            'temperature_morning_min', 'temperature_morning_max',
            'temperature_afternoon_min', 'temperature_afternoon_max',
            'temperature_night_min', 'temperature_night_max',
            'cloud_coverage_low', 'cloud_coverage_mid', 'cloud_coverage_high',
            'sunrise', 'sunset'
        ]