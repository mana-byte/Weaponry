from django import forms
from .models import Weapon, Place


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = '__all__'


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
