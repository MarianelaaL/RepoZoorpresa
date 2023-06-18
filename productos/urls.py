from django.urls import path
from .views import PetShop, Productos, SobreNosotros, Formulario, imc, Tablas, modificar, crear, crearcat, modificarcat,eliminar

urlpatterns=[
    path('', PetShop, name="PetShop"),
    path('Productos/', Productos, name="Productos"),
    path('SobreNosotros/', SobreNosotros, name="SobreNosotros"),
    path('Formulario/', Formulario, name="Formulario"),
    path('imc/', imc, name="imc"),
    path('Tablas/', Tablas, name="Tablas"),
    path('crear/', crear, name="crear"),
    path('crearcat/', crearcat, name="crearcat"),
    path('Modificar/<id>', modificar, name="modificar"),
    path('modificarcat/<id>', modificarcat, name="modificarcat"),
    path('eliminar/<id>', eliminar, name="eliminar"),
]