from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class RegistroUserForm(UserCreationForm):
    class Meta: 
        model=User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto','nro_producto', 'descripcion', 'categoria', 'precio', 'imagen']
        labels = {
            'nombre_producto' : 'Nombre de producto',
            'nro_producto' : "Nro producto",
            'descripcion' : "Descripcion",
            'categoria' : "Categoria",
            'precio' : "Precio",
            'imagen': "Imagen "
        }
        widgets={
            'nombre_producto' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el nombre del producto',
                    'class' : 'form-control',
                    'id' : 'nombre_producto'}
            ),
            'nro_producto' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese Id del producto',
                    'class' : 'form-control',
                    'id' : 'nro_producto'}
            ),
            'descripcion' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese la descripcion del producto',
                    'class' : 'form-control',
                    'id' : 'descripcion'}
            ),
            'categoria' : forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id' : 'categoria'}
            ),
            'precio' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el precio del producto',
                    'class' : 'form-control',
                    'id' : 'precio' }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class' : 'form-control',
                    'id' : 'imagen'
                }
            )
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['idCategoria', 'nombreCategoria']
        labels = {
            'idCategoria' : "Nro producto",
            'nombreCategoria' : "Nombre Categoria"
        }
        widgets={
            'idCategoria' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el id del producto',
                    'class' : 'form-control',
                    'id' : 'idCategoria' 
                }
            ),
            'nombreCategoria' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el nombre de la categoria del producto',
                    'class' : 'form-control',
                    'id' : 'nombreCategoria' 
                }
            )
        }
