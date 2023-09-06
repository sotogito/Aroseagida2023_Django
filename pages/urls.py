from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage),
    path('company/aroseagida/',views.aroseagida), #아로새기다?
    path('adventure', views.adventure), #게임 설명서
]
