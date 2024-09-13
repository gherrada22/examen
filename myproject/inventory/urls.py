from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/registrar/', views.registrar_producto, name='registrar_producto'),
    path('venta/', views.venta_pedido, name='venta_pedido'),
]