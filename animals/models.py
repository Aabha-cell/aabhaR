from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

genders =(
	('M','male'),
	('F','female'),
	('O','other')
	)
# Create your models here.
class Cat(models.Model):
	name = models.CharField(max_length = 200)
	breed = models.CharField(max_length = 200)
	age = models.IntegerField()
	weight = models.IntegerField()
	note = models.TextField()
	vaccinated = models.BooleanField()
	author = models.ForeignKey(User, default = None, on_delete=models.CASCADE)
	gender = models.CharField(max_length=3, choices =genders)

	def __str__(self):
		return self.name


class Dog(models.Model):
	name = models.CharField(max_length = 200)
	breed = models.CharField(max_length = 200)
	age = models.IntegerField()
	weight = models.IntegerField()
	note = models.TextField()
	vaccinated = models.BooleanField()
	author = models.ForeignKey(User, default = None, on_delete=models.CASCADE)
	gender = models.CharField(max_length=3, choices =genders)

	def __str__(self):
		return self.name