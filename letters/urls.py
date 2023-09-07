from django.urls import path

from.import views

urlpatterns = [
    path('mymail/',views.mymail),
    path('mymail/blockmail/',views.blockmail, name='myletter_blockmail'),
    path('<int:content_id>/', views.detail,name='detail'),
    path('comment/create/<int:content_id>/', views.comment_create, name='comment_create'),
    path('comment/update/<int:comment_id>/', views.comment_update,name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('mymail/is_active_update/<int:id>/', views.is_active_update, name='is_active_update'),

    #데이터 받기
    path('api/receive_unity_data/', views.receive_unity_data, name='receive_unity_data'),
    path('api/update_is_active/', views.update_is_active, name='update_is_active'),
    #데이터 보내기
    path('api/get_user_level/', views.get_user_level, name='get_user_level'),
    path('api/get_prevletter_list/', views.get_prevletter_list, name='get_prevletter_list'),
]