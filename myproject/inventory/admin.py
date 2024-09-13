from django.contrib import admin
from .models import Grupo, SubGrupo, Producto, Orden, DetalleVenta

admin.site.register(Grupo)
admin.site.register(SubGrupo)
admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(DetalleVenta)