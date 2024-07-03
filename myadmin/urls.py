from django.urls import path
from . import views

app_name = "myadmin"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path("auth/user/", views.custom_user_list, name="get_user"),
    path("db/cropyield/", views.custom_cropyield_list, name="cropyield"),
    path("db/cropreco/", views.custom_cropreco_list, name="cropreco"),
    path("db/fertreco/", views.custom_fertreco_list, name="fertreco"),
]