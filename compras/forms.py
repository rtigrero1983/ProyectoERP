from django import forms
from compras.models import Producto, Cliente, Factura, Detalle_factura


class ClienteForm(forms.ModelForm):
    class Meta:
          model = Cliente
          fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
          model = Producto
          fields = '__all__'
