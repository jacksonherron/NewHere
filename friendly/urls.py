from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('match/list/', views.match_list, name='match_list'),
    path('match/create', views.match_create, name='match_create'),
    path('match/detail', views.match_detail, name='match_detail')
]