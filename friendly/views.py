from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile, Match, Message
from random import randint
from django.db.models import Max

# Create your views here.

def base(request):
    return render(request, 'base.html')

def landing_page(request):
    return render(request, 'landing_page.html')

@login_required
def home(request):
    max_id = Profile.objects.all().aggregate(max_id=Max("id"))['max_id']
    while(True):
        pk = randint(1, max_id)
        try:
            profile = Profile.objects.get(pk=pk)
        except:
            profile = None
        if profile:
            if profile.user != request.user:
                break
    return render(request, 'home.html', {'profile': profile})

@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    if Profile.objects.filter(user=request.user).exists():
        profile = Profile.objects.get(user=request.user)
    else:
        profile = False
    if request.method == 'POST':
        if profile: 
            form = ProfileForm(request.POST, instance=profile)
        else:
            form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        if profile: 
            form = ProfileForm(instance=profile)
        else:
            form = ProfileForm()
        return render(request, 'profile_form.html', {'form': form})

@login_required
def match_create(request):
    #Search for an existing match, if so validate it, otherwise create a new match
    user_1 = Profile.objects.get(user=request.user)
    user_2 = Profile.objects.get(id=request.POST.get('profile_id'))
    print(user_1, user_2)
    # return HttpResponse('Finished')
    try:
        match = Match.objects.get(user_2=user_1)
    except:
        match = None
    if match:
        match.validate = True
        match.save()
        return HttpResponse('New match!')
    else:
        new_match = Match(user_1=user_1, user_2=user_2)
        new_match.save()
        return HttpResponse('Match request received.')

@login_required
def match_list(request):
    matches = Match.object.all()
    return render(request, 'match_list', {'matches': matches})