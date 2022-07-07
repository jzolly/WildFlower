from django.urls import path
from . import views # the '.' refers to referencing from the same folder we are in.

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flowers/', views.flowers_index, name='index'),
    path('flowers/<int:flower_id>/', views.flowers_detail, name='detail'),
    path('flowers/create/', views.FlowerCreate.as_view(), name='flowers_create'),
    path('flowers/<int:pk>/update/', views.FlowerUpdate.as_view(), name='flowers_update'),
    path('flowers/<int:pk>/delete/', views.FlowerDelete.as_view(), name='flowers_delete'),
    path('flowers/<int:flower_id>/add_sighting/', views.add_sighting, name='add_sighting'),
]