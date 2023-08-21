from django.urls import path

from.import views

urlpatterns = [
    path('mymail/',views.mymail),
    path('mymail/blockmail/',views.blockmail, name='myletter_blockmail'),
    #데이터 받기
    path('api/receive_unity_data/', views.receive_unity_data, name='receive_unity_data'),
    path('api/get_user_level/', views.get_user_level, name='get_user_level'),
]