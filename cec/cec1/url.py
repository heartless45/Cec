from django.urls import path
from . import views

urlpatterns = [
	path('',views.home),
	path('india/',views.india),
	path('Australia/',views.Australia),
	path('America/',views.America),
	path('india/gujarat/',views.Gandhinagar),
	path('india/maharashtra/',views.Maharashtra),
	path('india/karnataka/',views.Karnataka),
	path('Australia/new/',views.new),
	path('Australia/queens/',views.queen),
	path('Australia/Tsamnia/',views.Ts),
	path('America/Cali/',views.Cali),
	path('America/Flor/',views.Flor),
	path('America/Geo/',views.Geo),
]