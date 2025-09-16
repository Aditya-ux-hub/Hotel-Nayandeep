from django.shortcuts import render
from .models import Room
# Create your views here.



def home(req):
    room= Room.objects.all()
    context = {
        'rooms': room
    }
    return render(req, 'pages/home.html', context)

def about(req):
    return render(req, 'pages/about.html')

def contact(req):
    return render(req, 'pages/contact.html')

def room(req):
    room= Room.objects.all()
    context = {
        'rooms': room
    }
    return render(req, 'pages/room.html',context )

def dining(req):
    return render(req, 'pages/dining.html')



def roomsingle(req, pk):
    room= Room.objects.get(id=pk)
    rooms = Room.objects.all()
    context = {
        'room': room,
        'imgs' : rooms
    }
    return render(req, 'pages/roomD.html', context)