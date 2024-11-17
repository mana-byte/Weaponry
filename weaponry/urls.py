from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_weapon/<str:pk>/', views.update_weapon, name='update_weapon'),
    path('use_place/<str:pk>/', views.use_place, name='use_place'),
    path('move_all_to_place/<str:pk>/',
         views.move_all_to_place, name='move_all_to_place'),
]
