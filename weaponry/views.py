from django.shortcuts import render, get_object_or_404, redirect
from .models import Weapon, Place
from .forms import WeaponForm, PlaceForm


def index(request):
    weapon = Weapon.objects.all()
    places = Place.objects.all()
    return render(request, 'index.html', {"weapons": weapon, "places": places})


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
    return render(request, 'update_weapon.html', {"form": form})
