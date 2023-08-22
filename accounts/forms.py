from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AddUserProfile
import random
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date



class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

class AddUserProfileForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],  # 날짜 형식 지정
        validators=[
            MinValueValidator(limit_value=date(1900, 1, 1), message=('잘못된 정보입니다. 다시 입력해주세요.')),
            MaxValueValidator(limit_value=date.today, message=('잘못된 정보입니다.다시 입력해주세요.')),
        ]
    )
    user_unique_id = forms.CharField(max_length=6, required=False,widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_unique_id'].initial = self.get_user_unique_id()

    def get_user_unique_id(self):
        return random.randrange(100000, 1000000)

    class Meta:
        model = AddUserProfile
        fields = ('birthdate', 'user_unique_id')


'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.user_unique_id:
            self.instance.user_unique_id = self.get_user_unique_id()

    def save(self, commit=True):
        profile = super().save(commit=False)
        if not profile.user_unique_id:
            profile.user_unique_id = self.get_user_unique_id()
        if commit:
            profile.user = self.instance
            profile.save()
        return profile

    def get_user_unique_id(self):
        while True:
            new_unique_id = str(random.randint(100000, 999999))
            if not AddUserProfile.objects.filter(user_unique_id=new_unique_id).exists():
                return new_unique_id
'''


