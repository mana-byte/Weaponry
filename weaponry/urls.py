from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_weapon/<str:pk>/', views.update_weapon, name='update_weapon'),
]
