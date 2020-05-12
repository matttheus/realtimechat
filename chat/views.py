from django.shortcuts import render
from django.views.generic import View


class LobbyView(View):

    def get(self, request):
        return render(request, 'chat/lobby.html')


class RoomView(View):

    def get(self, request, room_name):
        
        context = {
            'room_name': room_name
        }

        return render(request, 'chat/room.html', context)