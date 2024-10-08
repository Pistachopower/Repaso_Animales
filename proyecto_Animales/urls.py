from django.urls import path
from . import views

urlpatterns = [
    path('', views.protectora_list, name= 'protectora_list'),
    path('animal', views.animal_list, name= 'animal_list'),
    path('colaborador', views.colaborador_list, name= 'colaborador_list')
]


