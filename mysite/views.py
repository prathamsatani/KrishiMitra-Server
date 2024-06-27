from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import (
    MyForm,
    LoginForm,
    FertilizerRecommenderForm,
    CropRecommenderForm,
    CropYieldPredictionForm,
    CustomUserCreationForm
)
from django.contrib.auth import login
from django.contrib import messages

def index(request):
    return render(request, "mysite/index.html")

def home(request):
    if request.COOKIES.get('username') is not None:
        return render(request, "mysite/home.html")
    else:
        return redirect('login')
    # return render(request, "mysite/home.html")


def about(request):
    return render(request, "mysite/about.html")


def yieldpred(request):
    if request.COOKIES.get('username') is not None:
        if request.method == "POST":
            form = CropYieldPredictionForm(request.POST)
            if form.is_valid():
                return render(request, "mysite/yieldpred.html", {"form": form})
        else:
            form = CropYieldPredictionForm()

        return render(request, "mysite/yieldpred.html", {"form": form})
    else:
        return redirect('login')

def fertpred(request):
    if request.COOKIES.get('username') is not None:
        if request.method == "POST":
            form = FertilizerRecommenderForm(request.POST)
            if form.is_valid():

                return render(request, "mysite/fertpred.html", {"form": form})
        else:
            form = FertilizerRecommenderForm()

        return render(request, "mysite/fertpred.html", {"form": form})
    else:
        return redirect('login')


def cropreco(request):
    if request.COOKIES.get('username') is not None:
        if request.method == "POST":
            form = CropRecommenderForm(request.POST)
            if form.is_valid():
                # Process the form data here
                # You can access form data using form.cleaned_data
                # Perform your crop recommendation logic
                # For now, we'll just render the same page
                return render(request, "mysite/cropreco.html", {"form": form})
        else:
            form = CropRecommenderForm()

        return render(request, "mysite/cropreco.html", {"form": form})
    else:
        return redirect('login')


def test(request):
    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            pass
    return render(request, "mysite/test.html", context={"form": form})


def login_view(request):
    if request.COOKIES.get('username') is not None:
        return redirect('home')
    else:
        if request.method == "POST":
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                if user is not None:
                    login(request, user)
                    response = redirect('home')   
                    response.set_cookie('username', user.username)
                    return response
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = LoginForm()
        return render(request, "mysite/login.html", {"form": form})


def signup_view(request):
    if request.COOKIES.get('username') is not None:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                response = redirect('home')
                response.set_cookie('username', user.username)
                return response
            else:
                messages.error(request, "Unsuccessful registration. Invalid information.")
        else:
            form = CustomUserCreationForm()
        return render(request, "mysite/signup.html", {"form": form})
    
def logout_view(request):
    response = redirect('index')
    response.delete_cookie('username')
    return response