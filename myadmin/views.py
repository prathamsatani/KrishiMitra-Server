from django.shortcuts import render, redirect
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model
import django.contrib.auth
from .forms import LoginForm, CreateUserForm
from django.contrib.auth.models import User
from krishimitra.models import (
    CropYield,
    CropRecommendation,
    FertilizerRecommendation,
    UserDataInput,
)
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


def logout(request):
    django.contrib.auth.logout(request)
    return redirect("myadmin:login")


def login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_superuser or user.is_staff:  # type: ignore
                    response = redirect("myadmin:home")
                    django.contrib.auth.login(request, user)
                    response.set_cookie("username", username)
                    return response
                else:
                    return render(request, "myadmin/accessdenied.html")
            else:
                return HttpResponse("Invalid login credentials")
        else:
            print(form.errors)
            print(form.non_field_errors())
            return HttpResponse("Invalid login")
    else:
        form = LoginForm()
    return render(request, "myadmin/login.html", {"form": form})


def home(request):
    if not request.user.is_authenticated:
        return redirect("myadmin:login")
    total_users = User.objects.count()
    yield_pred = CropYield.objects.count()
    crop_pred = CropRecommendation.objects.count()
    fert_pred = FertilizerRecommendation.objects.count()
    user_data = UserDataInput.objects.count()

    recent_activities = CropRecommendation.objects.order_by("-date")[:5]  # Assuming Prediction model has a timestamp field

    last_backup_date = (
        timezone.now()
    )  # Placeholder, replace with actual last backup date

    recent_actions = LogEntry.objects.select_related("content_type", "user")[:10]

    # Process the log entries to create more readable action descriptions
    processed_actions = []
    for action in recent_actions:
        content_type = action.content_type
        object_id = action.object_id
        try:
            object_repr = action.object_repr
        except:
            object_repr = "Unknown Object"

        if action.is_addition():
            action_type = "Added"
        elif action.is_change():
            action_type = "Modified"
        elif action.is_deletion():
            action_type = "Deleted"
        else:
            action_type = "Performed action on"

        # Create a link to the admin page for the object, if it exists
        if not action.is_deletion():
            try:
                admin_url = reverse(f"admin:{content_type.app_label}_{content_type.model}_change", args=[object_id])  # type: ignore
            except:
                admin_url = None
        else:
            admin_url = None

        processed_actions.append(
            {
                "user": action.user,
                "action_time": action.action_time,
                "action_type": action_type,
                "object_repr": object_repr,
                "model_name": content_type.model.capitalize(),  # type: ignore
                "admin_url": admin_url,
            }
        )

    last_login = request.user.last_login

    context = {
        "total_users": total_users,
        "yield_pred": yield_pred,
        "crop_pred": crop_pred,
        "fert_pred": fert_pred,
        "user_data": user_data,
        "recent_activities": recent_activities,
        "last_backup_date": last_backup_date,
    }

    return render(request, "myadmin/home.html", context)


@staff_member_required
def custom_user_list(request):
    User = get_user_model()
    users = User.objects.all().order_by("username")

    query = request.GET.get("q")
    if query:
        users = users.filter(username__icontains=query) | users.filter(
            email__icontains=query
        )

    paginator = Paginator(users, 20)  # Show 20 users per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "users": page_obj,
        "page_obj": page_obj,
        "paginator": paginator,
    }
    return render(request, "myadmin/userpage.html", context)


@login_required
def custom_cropyield_list(request):
    crop_yield_data = CropYield.objects.all().order_by("-date")

    search_query = request.GET.get("q")
    if search_query:
        crop_yield_data = (
            crop_yield_data.filter(username__icontains=search_query)
            | crop_yield_data.filter(state__icontains=search_query)
            | crop_yield_data.filter(season__icontains=search_query)
        )

    paginator = Paginator(crop_yield_data, 10)  # Show 10 entries per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    total_entries = CropYield.objects.count()
    unique_users = CropYield.objects.values("username").distinct().count()
    states_covered = CropYield.objects.values("state").distinct().count()
    seasons_recorded = CropYield.objects.values("season").distinct().count()

    context = {
        "crop_yield_data": page_obj,
        "page_obj": page_obj,
        "paginator": paginator,
        "search_query": search_query,
        "total_entries": total_entries,
        "unique_users": unique_users,
        "states_covered": states_covered,
        "seasons_recorded": seasons_recorded,
        "last_update": (
            CropYield.objects.latest("date").date
            if CropYield.objects.exists()
            else None
        ),
    }

    return render(request, "myadmin/cropyield.html", context)


@login_required
def custom_cropreco_list(request):
    crop_reco_data = CropRecommendation.objects.all().order_by("-date")

    search_query = request.GET.get("q")
    if search_query:
        crop_reco_data = (
            crop_reco_data.filter(username__icontains=search_query)
            | crop_reco_data.filter(state__icontains=search_query)
            | crop_reco_data.filter(season__icontains=search_query)
        )

    paginator = Paginator(crop_reco_data, 10)  # Show 10 entries per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    total_entries = CropRecommendation.objects.count()
    unique_users = CropRecommendation.objects.values("username").distinct().count()
    
    context = {
        "crop_yield_data": page_obj,
        "page_obj": page_obj,
        "paginator": paginator,
        "search_query": search_query,
        "total_entries": total_entries,
        "unique_users": unique_users,
        "last_update": (
            CropRecommendation.objects.latest("date").date
            if CropRecommendation.objects.exists()
            else None
        ),
    }

    return render(request, "myadmin/cropreco.html", context)


@login_required
def custom_fertreco_list(request):
    fert_reco_data = FertilizerRecommendation.objects.all().order_by("-date")

    search_query = request.GET.get("q")
    if search_query:
        fert_reco_data = (
            fert_reco_data.filter(username__icontains=search_query)
            | fert_reco_data.filter(state__icontains=search_query)
            | fert_reco_data.filter(season__icontains=search_query)
        )

    paginator = Paginator(fert_reco_data, 10)  # Show 10 entries per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    total_entries = FertilizerRecommendation.objects.count()
    unique_users = FertilizerRecommendation.objects.values("username").distinct().count()
    total_crops = FertilizerRecommendation.objects.values("crop").distinct().count()
    
    context = {
        "crop_yield_data": page_obj,
        "page_obj": page_obj,
        "paginator": paginator,
        "search_query": search_query,
        "total_entries": total_entries,
        "unique_users": unique_users,
        "total_crops": total_crops,
        "last_update": (
            FertilizerRecommendation.objects.latest("date").date
            if FertilizerRecommendation.objects.exists()
            else None
        ),
    }

    return render(request, "myadmin/fertpred.html", context)


def createUser(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect("myadmin:get_user")
    else:
        form = CreateUserForm()
    return render(request, "myadmin/adduser.html", {"form": form})