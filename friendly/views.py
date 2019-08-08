from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
    return render(request, 'base.html')

def landing_page(request):
    return render(request, 'landing_page.html')

# @login_required
def home(request):
    return render(request, 'home.html')

# @login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html')

# @login_required
def match_list(request):
    matches = Match.object.all()
    return render(request, 'match_list', {'matches': matches})