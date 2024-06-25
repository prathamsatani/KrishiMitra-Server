from django.db import models
from datetime import datetime
from django.utils import timezone


class CropYield(models.Model):
    username = models.CharField(max_length=100, unique=False)
    date = models.DateField(default=timezone.now, unique=False)
    name = models.CharField(max_length=100, unique=False)
    season = models.CharField(max_length=100, unique=False)
    state = models.CharField(max_length=100, unique=False)
    area = models.CharField(max_length=100, unique=False)
    annual_rainfall = models.CharField(max_length=100, unique=False)
    fertilizer_usage = models.CharField(max_length=100, unique=False)
    pesticide_usage = models.CharField(max_length=100, unique=False)


class CropRecommendation(models.Model):
    username = models.CharField(max_length=100, unique=False)
    date = models.DateField(default=timezone.now, unique=False)
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()


class FertilizerRecommendation(models.Model):
    username = models.CharField(max_length=100, unique=False)
    date = models.DateField(default=timezone.now, unique=False)
    soil_color = models.CharField(max_length=100, unique=False)
    nitrogen = models.CharField(max_length=100, unique=False)
    phosphorus = models.CharField(max_length=100, unique=False)
    potassium = models.CharField(max_length=100, unique=False)
    ph = models.CharField(max_length=100, unique=False)
    rainfall = models.CharField(max_length=100, unique=False)
    temperature = models.CharField(max_length=100, unique=False)
    crop = models.CharField(max_length=100, unique=False)


class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Signup(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class UserDataInput(models.Model):
    username = models.CharField(max_length=100, unique=False)
    date = models.DateField(default=timezone.now, unique=False)
    crop = models.CharField(max_length=100, unique=False)
    season = models.CharField(max_length=100, unique=False)
    state = models.CharField(max_length=100, unique=False)
    yield1 = models.CharField(max_length=100, unique=False)
    area = models.CharField(max_length=100, unique=False)
    rainfall = models.CharField(max_length=100, unique=False)
    fertilizer = models.CharField(max_length=100, unique=False)
    fertilizerQty = models.CharField(max_length=100, unique=False)
    pesticide = models.CharField(max_length=100, unique=False)
    pesticideQty = models.CharField(max_length=100, unique=False)
    nitrogen = models.CharField(max_length=100, unique=False)
    phosphorus = models.CharField(max_length=100, unique=False)
    potassium = models.CharField(max_length=100, unique=False)
    temperature = models.CharField(max_length=100, unique=False)
    humidity = models.CharField(max_length=100, unique=False)
    ph = models.CharField(max_length=100, unique=False)
    soilColor = models.CharField(max_length=100, unique=False)
