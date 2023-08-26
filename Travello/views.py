from django.shortcuts import render

from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.desc = 'The City that Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer=True
    
    dest2 = Destination()
    dest2.name = "Chennai"
    dest2.desc = "Its a Wonderful City"
    dest2.img='destination_2.jpg'
    dest2.price = 500
    dest2.offer=False
    
    dest3 = Destination()
    dest3.name = "Bangalore"
    dest3.desc = "City of Nights"
    dest3.img='destination_3.jpg'
    dest3.price = 800
    dest2.offer =True
    
    dests=[dest1,dest2,dest3]
    
    return render(request, 'index.html', {'dests':dests})
    
