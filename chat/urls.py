from django.urls import path

from chat import views

app_name = 'chat'

urlpatterns = [
    path('', views.LobbyView.as_view(), name='lobby'),
    path('<str:room_name>/', views.RoomView.as_view(), name='room'),
]