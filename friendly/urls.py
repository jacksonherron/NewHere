from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home, name='home'),
    path('profile/', views.home, name='home'),
]