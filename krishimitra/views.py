from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from krishimitra import models
from rest_framework import status
from .mlengine.main import predictYield, recommendCrop, recommendFertilizer
from krishimitra.models import CropYield
import logging
from .serializers import (
    CropYieldSerializer,
    CropRecommendationSerializer,
    FertilizerRecommendationSerializer,
    LoginSerializer,
    SignupSerializer,
    UserDataInputSerializer,
)

logger = logging.getLogger(__name__)


class CropYieldPrediction(APIView):
    def preprocess_data(
        self,
        name,
        season,
        state,
        area,
        annual_rainfall,
        fertilizer_usage,
        pesticide_usage,
    ):
        state_correlation = {
            "Assam": 0,
            "Karnataka": 1,
            "Meghalaya": 2,
            "West Bengal": 3,
            "Puducherry": 4,
            "Goa": 5,
            "Kerala": 6,
            "Andhra Pradesh": 7,
            "Tamil Nadu": 8,
            "Bihar": 9,
            "Gujarat": 10,
            "Maharashtra": 11,
            "Mizoram": 12,
            "Punjab": 13,
            "Uttar Pradesh": 14,
            "Haryana": 15,
            "Himachal Pradesh": 16,
            "Madhya Pradesh": 17,
            "Tripura": 18,
            "Nagaland": 19,
            "Odisha": 20,
            "Chhattisgarh": 21,
            "Uttarakhand": 22,
            "Jharkhand": 23,
            "Delhi": 24,
            "Manipur": 25,
            "Jammu and Kashmir": 26,
            "Telangana": 27,
            "Arunachal Pradesh": 28,
            "Sikkim": 29,
        }

        season_correlation = {
            "Autumn": 0,
            "Summer": 1,
            "Winter": 2,
            "Kharif": 3,
            "Rabi": 4,
            "Whole Year": 5,
        }

        crop_correlation = {
            "Arecanut": 0,
            "Arhar/Tur": 1,
            "Castor seed": 2,
            "Coconut ": 3,
            "Cotton(lint)": 4,
            "Dry chillies": 5,
            "Gram": 6,
            "Jute": 7,
            "Linseed": 8,
            "Maize": 9,
            "Mesta": 10,
            "Niger seed": 11,
            "Onion": 12,
            "Other  Rabi pulses": 13,
            "Potato": 14,
            "Rapeseed &Mustard": 15,
            "Rice": 16,
            "Sesamum": 17,
            "Small millets": 18,
            "Sugarcane": 19,
            "Sweet potato": 20,
            "Tapioca": 21,
            "Tobacco": 22,
            "Turmeric": 23,
            "Wheat": 24,
            "Bajra": 25,
            "Black pepper": 26,
            "Cardamom": 27,
            "Coriander": 28,
            "Garlic": 29,
            "Ginger": 30,
            "Groundnut": 31,
            "Horse-gram": 32,
            "Jowar": 33,
            "Ragi": 34,
            "Cashewnut": 35,
            "Banana": 36,
            "Soyabean": 37,
            "Barley": 38,
            "Khesari": 39,
            "Masoor": 40,
            "Moong(Green Gram)": 41,
            "Other Kharif pulses": 42,
            "Safflower": 43,
            "Sannhamp": 44,
            "Sunflower": 45,
            "Urad": 46,
            "Peas & beans (Pulses)": 47,
            "other oilseeds": 48,
            "Other Cereals": 49,
            "Cowpea(Lobia)": 50,
            "Oilseeds total": 51,
            "Guar seed": 52,
            "Other Summer Pulses": 53,
            "Moth": 54,
        }

        name = crop_correlation[name] + 1
        state = state_correlation[state]
        season = season_correlation[season]
        area = float(area)
        annual_rainfall = float(annual_rainfall)
        fertilizer_usage = float(fertilizer_usage)
        pesticide_usage = float(pesticide_usage)

        return [
            name,
            state,
            season,
            area,
            annual_rainfall,
            fertilizer_usage,
            pesticide_usage,
        ]

    def post(self, request):
        if request.method == "POST":
            serializer = CropYieldSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]  # type: ignore
                name = serializer.data["name"]  # type: ignore
                season = serializer.data["season"]  # type: ignore
                state = serializer.data["state"]  # type: ignore
                area = serializer.data["area"]  # type: ignore
                annual_rainfall = serializer.data["annual_rainfall"]  # type: ignore
                fertilizer_usage = serializer.data["fertilizer_usage"]  # type: ignore
                pesticide_usage = serializer.data["pesticide_usage"]  # type: ignore

                data = self.preprocess_data(
                    name,
                    season,
                    state,
                    area,
                    annual_rainfall,
                    fertilizer_usage,
                    pesticide_usage,
                )

                prediction = predictYield(data)

                crop_yield = CropYield(
                    username=username,
                    name=name,
                    season=season,
                    state=state,
                    area=area,
                    annual_rainfall=annual_rainfall,
                    fertilizer_usage=fertilizer_usage,
                    pesticide_usage=pesticide_usage,
                )
                crop_yield.save()
                return Response(round(prediction), status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CropRecommendation(APIView):

    def preprocess_data(
        self, nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall
    ):
        self.crop_correlation = {
            "rice": 0,
            "maize": 1,
            "chickpea": 2,
            "kidneybeans": 3,
            "pigeonpeas": 4,
            "mothbeans": 5,
            "mungbean": 6,
            "blackgram": 7,
            "lentil": 8,
            "pomegranate": 9,
            "banana": 10,
            "mango": 11,
            "grapes": 12,
            "watermelon": 13,
            "muskmelon": 14,
            "apple": 15,
            "orange": 16,
            "papaya": 17,
            "coconut": 18,
            "cotton": 19,
            "jute": 20,
            "coffee": 21,
        }

        return [
            int(nitrogen),
            int(phosphorous),
            int(potassium),
            float(temperature),
            float(humidity),
            float(ph),
            float(rainfall),
        ]

    def post(self, request):
        if request.method == "POST":
            serializer = CropRecommendationSerializer(data=request.data)
            if serializer.is_valid():
                # print(serializer.data)
                username = serializer.data["username"]  # type: ignore
                nitrogen = serializer.data["nitrogen"]  # type: ignore
                phosphorous = serializer.data["phosphorus"]  # type: ignore
                potassium = serializer.data["potassium"]  # type: ignore
                temperature = serializer.data["temperature"]  # type: ignore
                humidity = serializer.data["humidity"]  # type: ignore
                ph = serializer.data["ph"]  # type: ignore
                rainfall = serializer.data["rainfall"]  # type: ignore

                data = self.preprocess_data(
                    nitrogen,
                    phosphorous,
                    potassium,
                    temperature,
                    humidity,
                    ph,
                    rainfall,
                )

                crop = recommendCrop(data)

                crop_recommendation = models.CropRecommendation(
                    username=username,
                    nitrogen=nitrogen,
                    phosphorus=phosphorous,
                    potassium=potassium,
                    temperature=temperature,
                    humidity=humidity,
                    ph=ph,
                    rainfall=rainfall,
                )
                crop_recommendation.save()
                crop = list(self.crop_correlation.keys())[
                    list(self.crop_correlation.values()).index(crop)
                ]

                return Response(crop, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FertilizerRecommendation(APIView):
    def preprocess_data(
        self,
        soil_color,
        nitrogen,
        phosphorous,
        potassium,
        ph,
        rainfall,
        temperature,
        crop,
    ):
        self.soil_correlation = {
            "Black": 0,
            "Red ": 1,
            "Medium Brown": 2,
            "Dark Brown": 3,
            "Red": 4,
            "Light Brown": 5,
            "Reddish Brown": 6,
        }
        self.crop_correlation = {
            "Sugarcane": 0,
            "Jowar": 1,
            "Cotton": 2,
            "Rice": 3,
            "Wheat": 4,
            "Groundnut": 5,
            "Maize": 6,
            "Tur": 7,
            "Urad": 8,
            "Moong": 9,
            "Gram": 10,
            "Masoor": 11,
            "Soybean": 12,
            "Ginger": 13,
            "Turmeric": 14,
            "Grapes": 15,
        }
        self.fertilizer_correlation = {
            "Urea": 0,
            "DAP": 1,
            "MOP": 2,
            "10:26:26 NPK": 3,
            "SSP": 4,
            "Magnesium Sulphate": 5,
            "13:32:26 NPK": 6,
            "12:32:16 NPK": 7,
            "50:26:26 NPK": 8,
            "19:19:19 NPK": 9,
            "Chilated Micronutrient": 10,
            "18:46:00 NPK": 11,
            "Sulphur": 12,
            "20:20:20 NPK": 13,
            "Ammonium Sulphate": 14,
            "Ferrous Sulphate": 15,
            "White Potash": 16,
            "10:10:10 NPK": 17,
            "Hydrated Lime": 18,
        }

        soil_color = self.soil_correlation[soil_color]
        crop = self.crop_correlation[crop]

        return [
            soil_color,
            int(nitrogen),
            int(phosphorous),
            int(potassium),
            float(ph),
            int(rainfall),
            int(temperature),
            crop,
        ]

    def post(self, request):
        if request.method == "POST":
            serializer = FertilizerRecommendationSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]  # type: ignore
                soil_color = serializer.data["soil_color"]  # type: ignore
                nitrogen = serializer.data["nitrogen"]  # type: ignore
                phosphorous = serializer.data["phosphorus"]  # type: ignore
                potassium = serializer.data["potassium"]  # type: ignore
                ph = serializer.data["ph"]  # type: ignore
                rainfall = serializer.data["rainfall"]  # type: ignore
                temperature = serializer.data["temperature"]  # type: ignore
                crop = serializer.data["crop"]  # type: ignore

                data = self.preprocess_data(
                    soil_color,
                    nitrogen,
                    phosphorous,
                    potassium,
                    ph,
                    rainfall,
                    temperature,
                    crop,
                )

                fertilizer = recommendFertilizer(data)

                fertilizer_recommendation = models.FertilizerRecommendation(
                    username=username,
                    soil_color=soil_color,
                    nitrogen=nitrogen,
                    phosphorus=phosphorous,
                    potassium=potassium,
                    ph=ph,
                    rainfall=rainfall,
                    temperature=temperature,
                    crop=crop,
                )
                fertilizer_recommendation.save()
                fertilizer = list(self.fertilizer_correlation.keys())[
                    list(self.fertilizer_correlation.values()).index(fertilizer)
                ]

                return Response(fertilizer, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]  # type: ignore
                password = serializer.data["password"]  # type: ignore

                user = authenticate(username=username, password=password)
                if user is not None:
                    return Response("Login Successful", status=status.HTTP_200_OK)
                else:
                    return Response("Login Failed", status=status.HTTP_401_UNAUTHORIZED)


class Signup(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = SignupSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]  # type: ignore
                password = serializer.data["password"]  # type: ignore
                email = serializer.data["email"]  # type: ignore
                first_name = serializer.data["first_name"]  # type: ignore
                last_name = serializer.data["last_name"]  # type: ignore

                user = User.objects.create(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.set_password(password)

                user.save()
                return Response("201", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDataInput(APIView):
    def post(self, request):
        if request.method == "POST":
            serializer = UserDataInputSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.data["username"]  # type: ignore
                crop = serializer.data["crop"]  # type: ignore
                season = serializer.data["season"]  # type: ignore
                state = serializer.data["state"]  # type: ignore
                yield1 = serializer.data["yield1"]  # type: ignore
                area = serializer.data["area"]  # type: ignore
                rainfall = serializer.data["rainfall"]  # type: ignore
                fertilizer = serializer.data["fertilizer"]  # type: ignore
                fertilizerQty = serializer.data["fertilizerQty"]  # type: ignore
                pesticide = serializer.data["pesticide"]  # type: ignore
                pesticideQty = serializer.data["pesticideQty"]  # type: ignore
                nitrogen = serializer.data["nitrogen"]  # type: ignore
                phosphorus = serializer.data["phosphorus"]  # type: ignore
                potassium = serializer.data["potassium"]  # type: ignore
                temperature = serializer.data["temperature"]  # type: ignore
                humidity = serializer.data["humidity"]  # type: ignore
                ph = serializer.data["ph"]  # type: ignore
                soilColor = serializer.data["soilColor"]  # type: ignore

                user_data_input = models.UserDataInput(
                    username=username,
                    crop=crop,
                    season=season,
                    state=state,
                    yield1=yield1,
                    area=area,
                    rainfall=rainfall,
                    fertilizer=fertilizer,
                    fertilizerQty=fertilizerQty,
                    pesticide=pesticide,
                    pesticideQty=pesticideQty,
                    nitrogen=nitrogen,
                    phosphorus=phosphorus,
                    potassium=potassium,
                    temperature=temperature,
                    humidity=humidity,
                    ph=ph,
                    soilColor=soilColor,
                )
                user_data_input.save()
                return Response("201", status=status.HTTP_201_CREATED)
            else:
                logger.error(f"Serializer errors: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
