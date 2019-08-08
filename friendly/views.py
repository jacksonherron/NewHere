from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile, Match, Message

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
    profile = Profile.objects.get(user=user)
    return render(request, 'profile.html', {'profile': profile})

# @login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
        return render(request, 'profile_form.html', {'form': form})



# @login_required
def match_list(request):
    matches = Match.object.all()
    return render(request, 'match_list', {'matches': matches})