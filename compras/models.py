from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombres = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return "{}  -> {}  -> {}".format(self.nombres,self.apellido,self.email)


class Producto(models.Model):
    codigo_producto = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=100)
    precio = models.FloatField()

    def __str__(self):
        return " {} ".format(self.nombre_producto)


class Factura(models.Model):
    codigo_factura = models.CharField(max_length=20)
    fecha_factura = models.DateField()
    valor_factura = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return "{} -> {} -> {}".format(self.codigo_factura, self.valor_factura, self.cliente.nombres)


class Detalle_factura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    valor_items = models.FloatField()

    def __str__(self):
        return "{} -> {} ".format(self.factura, self.valor_items)
