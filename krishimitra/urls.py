from .views import CropYieldPrediction, CropRecommendation, FertilizerRecommendation, Login, Signup, UserDataInput 
from django.urls import path

urlpatterns = [
    path("yieldpred/", CropYieldPrediction.as_view(), name="yieldpred"),
    path("cropreco/", CropRecommendation.as_view(), name="cropreco"),
    path("fertreco/", FertilizerRecommendation.as_view(), name="fertreco"),
    path("userdatainput/", UserDataInput.as_view(), name="userdatainput"),
    path("login/", Login.as_view(), name="login"),
    path("signup/", Signup.as_view(), name="signup"),
]