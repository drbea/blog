from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from room.models import Room
from .serializers import RoomSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [

        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',

        'POST /api/rooms',
        'PUT /api/rooms/:id',
        'DELETE /api/rooms/:id',

    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, room_id):
    room = Room.objects.get(id = room_id)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)