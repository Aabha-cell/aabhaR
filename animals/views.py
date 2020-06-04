from django.shortcuts import render, redirect
from .models import Cat, Dog
from .forms import NewCat, NewDog
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def animal_list(request):
	return render(request, 'animals/animal_list.html', {})

def cat_list(request):
	cats = Cat.objects.all()
	return render(request, 'animals/cat_list.html', {'cats':cats})

def dog_list(request):
	dogs = Dog.objects.all()
	return render(request, 'animals/dog_list.html', {'dogs':dogs})

def new_cat(request):
    if request.method == "POST":
        form = NewCat(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.author = request.user
            cat.save()
            return redirect('/cat/',)
    else:
        form = NewCat()
    return render(request, 'animals/new_cat.html', {'form': form})

def new_dog(request):
    if request.method == "POST":
        form = NewDog(request.POST)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.author = request.user
            dog.save()
            return redirect('/dog/',)
    else:
        form = NewDog()
    return render(request, 'animals/new_dog.html', {'form': form})