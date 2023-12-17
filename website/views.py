from django.shortcuts import render, get_object_or_404
from website.models import *

# Create your views here.

def home(request):
    profile_objs = Profile.objects.all()
    context = {
        'profiles': profile_objs,
    }
    return render(request, "home.html", context)

def profile(request, profile_slug):
    profile_obj = get_object_or_404(Profile, slug=profile_slug)

    context = {
        'profile' : profile_obj,
    }

    return render(request, "profile.html", context)