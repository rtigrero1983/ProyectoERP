from django.shortcuts import render, redirect
from compras.models import Cliente, Producto
from django.http import HttpResponse
from compras.forms import ClienteForm, ProductoForm
# Create your views here.


def cargar_index(request):
    return render(request, "index.html")


def cargar_listado_cliente(request):
    cliente1 = Cliente.objects.all()
    return render(request, "listado_cliente.html", {'clientes': cliente1})

def crear_cliente_post(request):
        if request.method=='GET':
            formulario = ClienteForm()
            contexto = {
                'formulario': formulario
            }
            return render(request, "crear_cliente.html", contexto)
        else:
            formulario = ClienteForm(request.POST)
            contexto = {
                'form': formulario
            }
            #print(formulario)
            if formulario.is_valid():
                formulario.save()
            return redirect('consulta_cliente')

        #return render(request, "<html><head></head><body>Registro Ingresado Correctamente</body></html>", contexto)


def editar_cliente(request, id):
    cliente1 = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente1)
        contexto = {
                       'formulario': form
                       }
        return render(request, "crear_cliente.html", contexto)
    else:
        form = ClienteForm(request.POST, instance=cliente1)
        contexto = {
            'formulario': form
        }
        if form.is_valid():
            form.save()
            return redirect('consulta_cliente')
    return render(request, "crear_cliente.html", contexto)


def eliminar_cliente(request, id):
    cliente1 = Cliente.objects.get(id=id)
    cliente1.delete()
    return redirect('consulta_cliente')


def cargar_listado_productos(request):
    articulo1 = Producto.objects.all()
    return render(request, "listado_producto.html", {'articulos': articulo1})


def crear_producto(request):
    if request.method == 'GET':
        formulario = ProductoForm()
        contexto = {
            'formulario': formulario
        }
        return render(request, "crear_producto.html", contexto)
    else:
        formulario = ProductoForm(request.POST)
        contexto = {
            'form': formulario
        }
        # print(formulario)
        if formulario.is_valid():
            formulario.save()
        return redirect('consulta_producto')


def eliminar_producto(request, id):
    articulo1 = Producto.objects.get(id=id)
    articulo1.delete()
    return redirect('consulta_producto')


def editar_producto(request, id):
    articulo1 = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=articulo1)
        contexto = {
                       'formulario': form
                       }
        return render(request, "crear_producto.html", contexto)
    else:
        form = ProductoForm(request.POST, instance=articulo1)
        contexto = {
            'formulario': form
        }
        if form.is_valid():
            form.save()
            return redirect('consulta_producto')
    return render(request, "crear_producto.html", contexto)


def buscar_usuario(request):
    usuario = request.GET['usuario']
    clave = request.GET['clave']

    if (usuario=="" and  clave==""):
      cadena= "No ingreso los datos a consultar"
      return HttpResponse(cadena)
    else:
      data= Cliente.objects.filter(nombres=usuario, apellido=clave)
      return render(request, "Dashboard.html", {"datos": data, "usuario": usuario})


