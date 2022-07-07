from django.contrib import admin
from .models import Flower, Sighting

# Register your models here.
admin.site.register(Flower)
admin.site.register(Sighting)