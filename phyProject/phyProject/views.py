from phyApp.models import Simulation_Project , Video_Project
from django.shortcuts import render , HttpResponse


# Create your views here.

def home(request):
     return render(request ,'simulations.html')

def about(request):
     return render(request ,'about.html')

def hardware(request):
     return render(request ,'videos.html')
