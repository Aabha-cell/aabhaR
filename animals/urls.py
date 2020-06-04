from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('cat/', views.cat_list, name='cat_list'),
    path('dog/', views.dog_list, name='dog_list'),
    path('newcat/',views.new_cat, name='new_cat'),
    path('newdog/',views.new_dog, name='new_dog'),
]