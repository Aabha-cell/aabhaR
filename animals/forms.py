from django import forms

from .models import Cat, Dog

class NewCat(forms.ModelForm):

    class Meta:
        model = Cat
        fields = ('name','breed','age','weight','vaccinated','note')

class NewDog(forms.ModelForm):

    class Meta:
        model = Dog
        fields = ('name','breed','age','weight','vaccinated','note')