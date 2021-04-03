from django.shortcuts import render
# from django.template import loader
from django.http import HttpResponse

from .models import User, Access

def index(request):
	participants = User.objects.all()
	context = {'participants': participants}
	print(request.POST)
	return render(request, 'game/index.html', context)

def prologue(request):
	# context = {access = Access.objects.get(pk="LBQYED").c}
	participants = User.objects.all()
	context = {'participants': participants}
	return render(request, 'game/prologue.html', context)

def crime(request):
	participants = User.objects.all()
	context = {'participants': participants}
	return render(request, 'game/img_crime_scene.html', context)

def interrogation(request):
	participants = User.objects.all()
	context = {'participants': participants}
	return render(request, 'game/interrogation_room.html', context)

def form(request):
	participants = User.objects.all()
	context = {'participants': participants}
	return render(request, 'game/form.html', context)