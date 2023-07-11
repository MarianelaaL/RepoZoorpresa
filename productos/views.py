from django.shortcuts import render, redirect
from .models import Producto, Boleta, detalle_boleta
from .forms import ProductosForm, CategoriaForm
from django.contrib.auth.decorators import login_required as lr
from productos.compra import Carrito

def PetShop(request):

    return render(request,'main/PetShop.html')

def Productos(request):
    cositas=Producto.objects.all()
    datos={
        'cositas':cositas
    }
    return render(request,'main/Productos.html', datos)


def SobreNosotros(request):
    
    return render(request,'main/SobreNosotros.html')

def Formulario(request):
    
    return render(request,'main/Formulario.html')

def imc(request):
    
    return render(request,'proce/imc.html')

def Tablas(request):
    productos = Producto.objects.raw('select * from productos_producto')
    datos = {'productos' : productos}
    return render(request,'proce/Tablas.html', datos)
@lr
def crear(request):
    if request.method=="POST":
        productoform = ProductosForm(request.POST,request.FILES)
        if productoform.is_valid():
            productoform.save() 
            return redirect ('crear')
    else:
        productoform=ProductosForm()
    return render(request, 'crear/crear.html', {'productoform' : productoform})

@lr
def eliminar(request, id):
    prodcutoEliminado=Producto.objects.get(nro_producto=id) #buscamos un vehiculo por la patentes
    prodcutoEliminado.delete()
    return redirect('Tablas')

@lr
def modificar(request,id):
    productoModif = Producto.objects.get(nro_producto=id)
    if request.method=="POST":    
        formulario = ProductosForm(request.POST, request.FILES, instance=productoModif)
        if formulario.is_valid():
            formulario.save()           #modificamos el objeto
            return redirect('Tablas')
    else:
        formulario = ProductosForm(instance=productoModif)

    datos = {
        'form': formulario
    }
    return render(request,'modificar/modificar.html', datos)


@lr
def crearcat(request):
    if request.method=="POST":
        categoriaForm = CategoriaForm(request.POST,request.FILES) #creamos un objeto de tipo form para vehiculos
        if categoriaForm.is_valid():
            categoriaForm.save() #similar en funcion al metodo insert
            return redirect ('crearcat')
    else:
        categoriaForm=CategoriaForm()
    return render(request, 'crear/crearcat.html', {'CategoriaForm' : CategoriaForm})

@lr
def modificarcat(request,id):
    productoModifCat = CategoriaForm.objects.get(nro_producto=id)
    datos ={
        'form': CategoriaForm(instance=productoModifCat)   #el objeto form llega al template
    }
    if request.method=="POST":          #modificamos backend con los cambios realizados
        formulario = CategoriaForm(data=request.POST, instance=productoModifCat)
        if formulario.is_valid():
            formulario.save()           #modificamos el objeto
            return redirect('modificarcat')
    return render(request,'modificar/modificarcat.html', datos)

def Tienda(request):
    cositas = Producto.objects.all()
    datos={
        'cosita':cositas
    }
    return render(request,'main/Tienda.html', datos)

def agregar_producto(request,id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(nro_producto=id)
    carrito_compra.agregar(producto=producto)
    return redirect('Tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(nro_producto=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('Tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(nro_producto=id)
    carrito_compra.restar(producto=producto)
    return redirect('Tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('Tienda')    

def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(nro_producto = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)