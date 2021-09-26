from django.contrib import admin

# Register your models here.

from .models import Simulation_Project , Video_Project
admin.site.register(Simulation_Project),
admin.site.register(Video_Project)

