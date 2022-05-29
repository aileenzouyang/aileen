from django.shortcuts import render
from travel.models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'Test Description'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Beijing'
    dest2.desc = 'Best city in the world'
    dest2.img = 'destination_2.jpg'
    dest2.price = 100000
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Apple Valley'
    dest3.desc = 'Where I am right now'
    dest3.img = 'destination_3.jpg'
    dest3.price = 7000
    dest3.offer = False

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html',{'dests': dests})
