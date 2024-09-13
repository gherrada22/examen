from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProductoForm, OrdenForm, DetalleVentaForm
from .models import Producto, Grupo, SubGrupo, Orden, DetalleVenta
from django.db.models import Q

@login_required
def lista_productos(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) |
            Q(subgrupo__nombre__icontains=query) |
            Q(subgrupo__grupo__nombre__icontains=query)
        )
    else:
        productos = Producto.objects.all()
    return render(request, 'inventory/lista_productos.html', {'productos': productos})


@login_required
def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'inventory/registrar_producto.html', {'form': form})

@login_required
def venta_pedido(request):
    if request.method == 'POST':
        orden_form = OrdenForm(request.POST)
        detalle_form = DetalleVentaForm(request.POST)
        if orden_form.is_valid() and detalle_form.is_valid():
            orden = orden_form.save()
            detalle = detalle_form.save(commit=False)
            detalle.orden = orden
            detalle.save()
            return redirect('lista_productos')
    else:
        orden_form = OrdenForm()
        detalle_form = DetalleVentaForm()
    return render(request, 'inventory/venta_pedido.html', {'orden_form': orden_form, 'detalle_form': detalle_form})