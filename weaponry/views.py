from django.shortcuts import render
from .models import Weapon, Place


def index(request):
    weapon = Weapon.objects.all()
    places = Place.objects.all()
    return render(request, 'index.html', {"weapons": weapon, "places": places})
