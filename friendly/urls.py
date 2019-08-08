from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('match_list/', views.match_list, name='match_list'),
]