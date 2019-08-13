from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, MessageForm
from .models import Profile, Match, Message
from random import randint
from django.db.models import Max

# Create your views here.

def base(request):
    return render(request, 'base.html')

def landing_page(request):
    return render(request, 'landing_page.html')

def about(request):
    return render(request, 'about.html')

@login_required
def home(request):
    user_profile = Profile.objects.get(user=request.user)
    other_profiles = Profile.objects.exclude(user=request.user).order_by('?')
    primary_matches = user_profile.primary_matches.values_list('user_2', flat=True)
    secondary_matches = user_profile.secondary_matches.filter(validate=True).values_list('user_1', flat=True)

    for profile in other_profiles:
        if (profile.id not in primary_matches) and (profile.id not in secondary_matches):
            return render(request, 'home.html', {'profile': profile})
    return render(request, 'home.html', {'profile': None})

@login_required
def profile(request):
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
    try:
        match = Match.objects.get(user_1=user_2, user_2=user_1)
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
    user = Profile.objects.get(user=request.user)
    try:
        primary_matches = Match.objects.filter(user_1=user, validate=True)
    except: 
        primary_matches = None
    try:
        secondary_matches = Match.objects.filter(user_2=user, validate=True)
    except:
        secondary_matches = None
    return render(request, 'match_list.html', {'primary_matches': primary_matches, 'secondary_matches': secondary_matches})

@login_required
def match_detail(request, pk):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    match = Match.objects.get(id=pk)
    try:
        messages = Message.objects.filter(match=match)            
    except:
        messages = None
    if match.user_1 == user_profile:
        match_profile = match.user_2
    else:
        match_profile = match.user_1
    return render(request, 'match_detail.html', {'match_profile': match_profile, 'match': match, 'messages': messages})

@login_required
def message_create(request, pk):
    author = Profile.objects.get(user=request.user)
    match = Match.objects.get(id=pk)
    content = request.POST.get("message_content")
    message = Message(author=author, match=match, content=content)
    message.save()
    return redirect('match_detail', pk)
