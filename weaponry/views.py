from django.shortcuts import render, get_object_or_404, redirect
from .models import Weapon, Place
from .forms import WeaponForm, PlaceForm


def index(request):
    weapon = Weapon.objects.all()
    places = Place.objects.all()
    total_earnings = 0
    for place in places:
        total_earnings += place.earnings
    return render(request, 'index.html', {"weapons": weapon, "places": places, "total_earnings": total_earnings})


def update_weapon(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    print("works")
    if request.method == "POST":
        form = WeaponForm(request.POST, instance=weapon)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WeaponForm(instance=weapon)
    return render(request, 'update_weapon.html', {"form": form, "weapon": weapon})


def use_place(request, pk):
    place = get_object_or_404(Place, pk=pk)
    weapons = Weapon.objects.all()
    place.use_facility(weapons)
    return redirect('index')


def move_all_to_place(request, pk):
    weapons = Weapon.objects.all()
    place = get_object_or_404(Place, pk=pk)
    for weapon in weapons:
        weapon.place = place
        weapon.save()
    return redirect('index')
