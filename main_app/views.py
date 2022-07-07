from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flower
from .forms import SightingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def flowers_index(request):
    flowers = Flower.objects.all()
    return render(request, 'flowers/index.html', {'flowers': flowers})

def flowers_detail(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    sighting_form = SightingForm()
    return render(request, 'flowers/detail.html', 
    {'flower': flower, 'sighting_form': sighting_form })

def add_sighting(request, flower_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.flower_id = flower_id
        new_sighting.save()
    return redirect('detail', flower_id=flower_id)

# CUDs
class FlowerCreate(CreateView):
    model = Flower
    fields = '__all__'
    success_url = '/flowers/'

class FlowerUpdate(UpdateView):
    model = Flower
    fields = '__all__'

class FlowerDelete(DeleteView):
    model = Flower
    success_url = '/flowers/'