from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('prologue/', views.prologue, name='prologue'),
	path('crime/', views.crime, name='crime'),
	path('interrogation/', views.interrogation, name='interrogation'),
	path('form/', views.form, name='form'),
]