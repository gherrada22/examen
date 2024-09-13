from django.db import models

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)

class SubGrupo(models.Model):
    nombre = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    subgrupo = models.ForeignKey(SubGrupo, on_delete=models.CASCADE)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)

class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)

class DetalleVenta(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)