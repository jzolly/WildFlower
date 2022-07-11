from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Flower, Use
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
    uses_flower_doesnt_have = Use.objects.exclude(id__in = flower.uses.all().values_list('id'))
    sighting_form = SightingForm()
    return render(request, 'flowers/detail.html', 
    {'flower': flower, 'sighting_form': sighting_form, 'uses': uses_flower_doesnt_have })

def add_sighting(request, flower_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.flower_id = flower_id
        new_sighting.save()
    return redirect('detail', flower_id=flower_id)

# Many-Many view methods
def assoc_use(request, flower_id, use_id):
    Flower.objects.get(id=flower_id).uses.add(use_id)
    return redirect('detail', flower_id=flower_id)

def assoc_use_delete(request, flower_id, use_id):
    Flower.objects.get(id=flower_id).uses.remove(use_id)
    return redirect('detail', flower_id=flower_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# CUDs Class Views
class FlowerCreate(CreateView):
    model = Flower
    fields = ['name', 'common_name', 'type', 'color', 'petals', 'size', 'leaf_arrangement', 'habitat', 'img']
    success_url = '/flowers/'

    def form_valid(self, form):
        form.instsance.user = self.request.user
        return super().form_valid(form)
    
class FlowerUpdate(UpdateView):
    model = Flower
    fields = ['name', 'common_name', 'type', 'color', 'petals', 'size', 'leaf_arrangement', 'habitat', 'img']

class FlowerDelete(DeleteView):
    model = Flower
    success_url = '/flowers/'

# Use Class Views

class UseList(ListView):
    model = Use
    template_name = 'uses/index.html'
class UseDetail(DetailView):
    model = Use
    template_name = 'uses/detail.html'
class UseCreate(CreateView):
    model = Use
    fields = ['name', 'use']  
class UseUpdate(UpdateView):
    model = Use
    fields = ['name', 'use']
class UseDelete(DeleteView):
    model = Use
    success_url ='/uses/'