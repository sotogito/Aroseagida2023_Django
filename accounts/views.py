from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm,AddUserProfileForm
from .models import AddUserProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date
from datetime import datetime


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
    user = AddUserProfile.objects.filter(id = 16).first() #임의의 사용자를 지정
    user_birthdate = user.birthdate
    now_date = datetime.now().date()
    user_age = now_date.year - user_birthdate.year - ((now_date.month, now_date.day) < (user_birthdate.month, user_birthdate.day))
    user_age_num = user_age // 10

    context = {
        'user_age' : user_age, #나이
        'user_age_num' : user_age_num #나이대를 계산할 값
    }
    return Response(context)













