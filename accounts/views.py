from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm,AddUserProfileForm
from datetime import date
from .models import AddUserProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        profile_form = AddUserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            #profile.user_unique_id = profile_form.get_user_unique_id()
            profile.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
        profile_form = AddUserProfileForm()
    return render(request, 'accounts/signup.html',{'form': form, 'profile_form': profile_form})




@api_view(['GET'])
def get_user_age(request):
    user = AddUserProfile.objects.filter(id = 13).first()
    a = user.birthdate.year

    b = 2
    context = {
        'a' : a,
        'b' : b
    }
    return Response(context)













