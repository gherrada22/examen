from django import forms
from .models import Producto, Orden, DetalleVenta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'subgrupo', 'precio_venta']

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['id_orden']

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio_venta']