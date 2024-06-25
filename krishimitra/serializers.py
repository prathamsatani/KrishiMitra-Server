from rest_framework import serializers
from .models import CropYield, CropRecommendation, FertilizerRecommendation, Login, Signup, UserDataInput


class CropYieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropYield
        fields = ["username", "name", "season", "state", "area", "annual_rainfall", "fertilizer_usage", "pesticide_usage"]


class CropRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropRecommendation
        fields = ["username", "nitrogen", "phosphorus", "potassium", "temperature", "humidity", "ph", "rainfall"]


class FertilizerRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FertilizerRecommendation
        fields = ["username","soil_color", "nitrogen", "phosphorus", "potassium", "ph", "rainfall", "temperature", "crop"]


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ["username", "password"]

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ["email", "username", "first_name", "last_name", "password"]

class UserDataInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDataInput
        fields = ["username", "crop", "season", "state", "yield1", "area", "rainfall",  "fertilizer", "fertilizerQty", "pesticide", "pesticideQty", "nitrogen", "phosphorus", "potassium", "temperature", "humidity", "ph", "soilColor"]