from django.contrib import admin
from .models import CropYield, CropRecommendation, FertilizerRecommendation, UserDataInput

admin.site.register(CropYield)
admin.site.register(CropRecommendation)
admin.site.register(FertilizerRecommendation)
admin.site.register(UserDataInput)