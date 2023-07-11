from django.urls import path
from .views import *

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

    path('Tienda/',Tienda, name="Tienda"),
    path('Tienda/',Tienda, name="Tienda"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]