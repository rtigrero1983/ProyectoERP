"""ERP1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from compras.views import crear_cliente_post, cargar_index, cargar_listado_cliente, editar_cliente, eliminar_cliente, \
                                cargar_listado_productos, crear_producto, eliminar_producto, editar_producto, buscar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cargar_index, name="index"),
    path('crear_cliente/', crear_cliente_post, name="crear_cliente"),
    path('consulta_cliente/', cargar_listado_cliente, name="consulta_cliente"),
    path('editar_cliente/<int:id>/', editar_cliente, name="editar_cliente"),
    path('eliminar_cliente/<int:id>/', eliminar_cliente, name="eliminar_cliente"),
    path('consulta_producto/', cargar_listado_productos, name="consulta_producto"),
    path('crear_producto/', crear_producto, name="crear_producto"),
    path('eliminar_producto/<int:id>/', eliminar_producto, name="eliminar_producto"),
    path('editar_producto/<int:id>/', editar_producto, name="editar_producto"),
    path('buscar_usuario/', buscar_usuario, name="buscar_usuario"),

]
