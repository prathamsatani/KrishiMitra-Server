from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line for the root URL
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("yieldpred/", views.yieldpred, name='yieldpred'),
    path("fertpred/", views.fertpred, name='fertpred'),
    path("cropreco/", views.cropreco, name='cropreco'),
    path("test/", views.test, name='test'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]