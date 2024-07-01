from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import (
    MyForm,
    LoginForm,
    FertilizerRecommenderForm,
    CropRecommenderForm,
    CropYieldPredictionForm,
    CustomUserCreationForm,
    UserDataInputForm
)
from krishimitra import models
from django.contrib.auth import login
from django.contrib import messages
from krishimitra.mlengine import main
from .postprocessing import (
    getNamesForYieldPred,
    getNamesForCropReco,
    getNamesForFertReco,
)


def index(request):
    if request.COOKIES.get("username") is not None:
        return redirect("home")
    else:
        return render(request, "mysite/index.html")


def home(request):
    if request.COOKIES.get("username") is not None:
        return render(request, "mysite/home.html")
    else:
        return redirect("login")
    # return render(request, "mysite/home.html")


def about(request):
    return render(request, "mysite/about.html")


def yieldpred(request):
    if request.COOKIES.get("username") is not None:
        if request.method == "POST":
            form = CropYieldPredictionForm(request.POST)
            if form.is_valid():
                username = request.COOKIES.get("username")
                crop = int(form.cleaned_data.get("crop")) + 1  # type: ignore
                season = int(form.cleaned_data.get("season"))  # type: ignore
                state = int(form.cleaned_data.get("state"))  # type: ignore
                area = float(form.cleaned_data.get("area"))  # type: ignore
                annual_rainfall = float(form.cleaned_data.get("annual_rainfall"))  # type: ignore
                fertilizer_usage = float(form.cleaned_data.get("fertilizer_usage"))  # type: ignore
                pesticide_usage = float(form.cleaned_data.get("pesticide_usage"))  # type: ignore

                data = [
                    crop,
                    season,
                    state,
                    area,
                    annual_rainfall,
                    fertilizer_usage,
                    pesticide_usage,
                ]

                prediction = round(main.predictYield(data) * area, 3)

                models.CropYield(
                    username=username,
                    name=getNamesForYieldPred(crop, season, state)["crop"],
                    season=getNamesForYieldPred(crop, season, state)["season"],
                    state=getNamesForYieldPred(crop, season, state)["state"],
                    area=area,
                    annual_rainfall=annual_rainfall,
                    fertilizer_usage=fertilizer_usage,
                    pesticide_usage=pesticide_usage,
                ).save()

                text = "Predicted yield according to the given conditions is " + str(prediction) + " tonnes."

                return render(
                    request,
                    "mysite/yieldpred.html",
                    {"form": form, "prediction": text},
                )
        else:
            form = CropYieldPredictionForm()

        return render(
            request, "mysite/yieldpred.html", {"form": form, "prediction": None}
        )
    else:
        return redirect("login")


def fertpred(request):
    if request.COOKIES.get("username") is not None:
        if request.method == "POST":
            form = FertilizerRecommenderForm(request.POST)
            if form.is_valid():
                username = request.COOKIES.get("username")
                soil_color = int(form.cleaned_data.get("soil"))  # type: ignore
                nitrogen = float(form.cleaned_data.get("nitrogen"))  # type: ignore
                phosphorus = float(form.cleaned_data.get("phosphorus"))  # type: ignore
                potassium = float(form.cleaned_data.get("potassium"))  # type: ignore
                ph = float(form.cleaned_data.get("ph"))  # type: ignore
                rainfall = float(form.cleaned_data.get("rainfall"))  # type: ignore
                temperature = float(form.cleaned_data.get("temperature"))  # type: ignore
                crop = int(form.cleaned_data.get("crop"))  # type: ignore

                data = [
                    soil_color,
                    nitrogen,
                    phosphorus,
                    potassium,
                    ph,
                    rainfall,
                    temperature,
                    crop,
                ]

                prediction = main.recommendFertilizer(data)

                print(data)

                prediction = getNamesForFertReco(soil_color, crop, prediction)[
                    "fertilizer"
                ]

                models.FertilizerRecommendation(
                    username=username,
                    soil_color=getNamesForFertReco(soil_color, crop, 0)["soil"],
                    nitrogen=nitrogen,
                    phosphorus=phosphorus,
                    potassium=potassium,
                    ph=ph,
                    rainfall=rainfall,
                    temperature=temperature,
                    crop=getNamesForFertReco(soil_color, crop, 0)["crop"],
                ).save()

                text = "Most suitable fertilizer according to the given conditions is " + str.upper(prediction) + "."

                return render(
                    request,
                    "mysite/fertpred.html",
                    {"form": form, "prediction": text},
                )
        else:
            form = FertilizerRecommenderForm()

        return render(
            request, "mysite/fertpred.html", {"form": form, "prediction": None}
        )
    else:
        return redirect("login")


def cropreco(request):
    if request.COOKIES.get("username") is not None:
        if request.method == "POST":
            form = CropRecommenderForm(request.POST)
            if form.is_valid():
                username = request.COOKIES.get("username")
                nitrogen = float(form.cleaned_data.get("nitrogen"))  # type: ignore
                phosphorus = float(form.cleaned_data.get("phosphorus"))  # type: ignore
                potassium = float(form.cleaned_data.get("potassium"))  # type: ignore
                ph = float(form.cleaned_data.get("ph"))  # type: ignore
                rainfall = float(form.cleaned_data.get("rainfall"))  # type: ignore
                temperature = float(form.cleaned_data.get("temperature"))  # type: ignore
                humidity = float(form.cleaned_data.get("humidity"))  # type: ignore

                data = [
                    nitrogen,
                    phosphorus,
                    potassium,
                    ph,
                    rainfall,
                    temperature,
                    humidity,
                ]

                prediction = main.recommendCrop(data)

                prediction = getNamesForCropReco(prediction)

                models.CropRecommendation(
                    username=username,
                    nitrogen=nitrogen,
                    phosphorus=phosphorus,
                    potassium=potassium,
                    ph=ph,
                    rainfall=rainfall,
                    temperature=temperature,
                    humidity=humidity,
                ).save()
                
                text = "Most suitable crop according to the given conditions is " + str.upper(prediction) + "."

                return render(
                    request,
                    "mysite/cropreco.html",
                    {"form": form, "prediction": text},
                )
        else:
            form = CropRecommenderForm()

        return render(
            request, "mysite/cropreco.html", {"form": form, "prediction": None}
        )
    else:
        return redirect("login")


def login_view(request):
    if request.COOKIES.get("username") is not None:
        return redirect("home")
    else:
        if request.method == "POST":
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                if user is not None:
                    login(request, user)
                    response = redirect("home")
                    response.set_cookie("username", user.username)
                    return response
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = LoginForm()
        return render(request, "mysite/login.html", {"form": form})


def signup_view(request):
    if request.COOKIES.get("username") is not None:
        return redirect("home")
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                response = redirect("home")
                response.set_cookie("username", user.username)
                return response
            else:
                messages.error(
                    request, "Unsuccessful registration. Invalid information."
                )
        else:
            form = CustomUserCreationForm()
        return render(request, "mysite/signup.html", {"form": form})


def userDataCollection(request): 
    if request.COOKIES.get("username") is not None:
        if request.method == "POST":
            form = UserDataInputForm(request.POST)
            if form.is_valid():
                username = request.COOKIES.get("username")
                crop = form.cleaned_data.get("crop")
                season = form.cleaned_data.get("season")
                state = form.cleaned_data.get("state")
                yield1 = form.cleaned_data.get("yield1")
                area = form.cleaned_data.get("area")
                rainfall = form.cleaned_data.get("rainfall")
                fertilizer = form.cleaned_data.get("fertilizer")
                fertilizerQty = form.cleaned_data.get("fertilizerQty")
                pesticide = form.cleaned_data.get("pesticide")
                pesticideQty = form.cleaned_data.get("pesticideQty")
                nitrogen = form.cleaned_data.get("nitrogen")
                phosphorus = form.cleaned_data.get("phosphorus")
                potassium = form.cleaned_data.get("potassium")
                temperature = form.cleaned_data.get("temperature")
                humidity = form.cleaned_data.get("humidity")
                ph = form.cleaned_data.get("ph")
                soilColor = form.cleaned_data.get("soilColor")
                
                models.UserDataInput(
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
                    soilColor=soilColor
                ).save()

                return redirect("home")
        else:
            form = UserDataInputForm()
        return render(request, "mysite/userdata.html", {"form": form})
    else:
        return redirect("login")


def logout_view(request):
    response = redirect("index")
    response.delete_cookie("username")
    return response
