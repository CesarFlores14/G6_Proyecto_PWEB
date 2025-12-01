from django.shortcuts import render, get_object_or_404, redirect
from .models import Plato, Mesa, Pedido, DetallePedido
from .forms import PlatoForm, MesaForm, PedidoForm, DetallePedidoForm

# VISTAS PARA PLATO
def listar_platos(request):
    platos = Plato.objects.all()
    return render(request, 'listar_platos.html', {'platos': platos})

def crear_plato(request):
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            Plato.objects.create(
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                categoria=form.cleaned_data['categoria'],
                disponible=form.cleaned_data['disponible']
            )
            return redirect('listar_platos')
    else:
        form = PlatoForm()
    return render(request, 'nuevo_plato.html', {'form': form})

def actualizar_plato(request, id):
    plato = get_object_or_404(Plato, id_plato=id)
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            plato.descripcion = form.cleaned_data['descripcion']
            plato.precio = form.cleaned_data['precio']
            plato.categoria = form.cleaned_data['categoria']
            plato.disponible = form.cleaned_data['disponible']
            plato.save()
            return redirect('listar_platos')
    else:
        form = PlatoForm(initial={
            'descripcion': plato.descripcion,
            'precio': plato.precio,
            'categoria': plato.categoria,
            'disponible': plato.disponible,
        })
    return render(request, 'actualizar_plato.html', {'form': form})

def eliminar_plato(request, id):
    plato = get_object_or_404(Plato, id_plato=id)
    plato.delete()
    return redirect('listar_platos')

# VISTAS PARA MESA
def listar_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'listar_mesas.html', {'mesas': mesas})

def crear_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            Mesa.objects.create(
                estado=form.cleaned_data['estado'],
                ubicacion=form.cleaned_data['ubicacion']
            )
            return redirect('listar_mesas')
    else:
        form = MesaForm()
    return render(request, 'nuevo_mesa.html', {'form': form})

def actualizar_mesa(request, id):
    mesa = get_object_or_404(Mesa, id_mesa=id)
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            mesa.estado = form.cleaned_data['estado']
            mesa.ubicacion = form.cleaned_data['ubicacion']
            mesa.save()
            return redirect('listar_mesas')
    else:
        form = MesaForm(initial={
            'estado': mesa.estado,
            'ubicacion': mesa.ubicacion,
        })
    return render(request, 'actualizar_mesa.html', {'form': form})

def eliminar_mesa(request, id):
    mesa = get_object_or_404(Mesa, id_mesa=id)
    mesa.delete()
    return redirect('listar_mesas')

# VISTAS PARA PEDIDO
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'listar_pedidos.html', {'pedidos': pedidos})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            mesa = get_object_or_404(Mesa, id_mesa=form.cleaned_data['id_mesa'])
            Pedido.objects.create(
                estadoped=form.cleaned_data['estadoped'],
                cliente=form.cleaned_data['cliente'],
                fecha=form.cleaned_data['fecha'],
                hora=form.cleaned_data['hora'],
                notas=form.cleaned_data['notas'],
                id_mesa=mesa
            )
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'nuevo_pedido.html', {'form': form})

def actualizar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id_pedido=id)
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            mesa = get_object_or_404(Mesa, id_mesa=form.cleaned_data['id_mesa'])
            pedido.estadoped = form.cleaned_data['estadoped']
            pedido.cliente = form.cleaned_data['cliente']
            pedido.fecha = form.cleaned_data['fecha']
            pedido.hora = form.cleaned_data['hora']
            pedido.notas = form.cleaned_data['notas']
            pedido.id_mesa = mesa
            pedido.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm(initial={
            'estadoped': pedido.estadoped,
            'cliente': pedido.cliente,
            'fecha': pedido.fecha,
            'hora': pedido.hora,
            'notas': pedido.notas,
            'id_mesa': pedido.id_mesa.id_mesa,
        })
    return render(request, 'actualizar_pedido.html', {'form': form})

def eliminar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id_pedido=id)
    pedido.delete()
    return redirect('listar_pedidos')
# VISTAS PARA DETALLE PEDIDO
def listar_detalles_pedido(request):
    detalles = DetallePedido.objects.all()
    return render(request, 'detalle_pedido.html', {'detalles': detalles})

def crear_detalle_pedido(request):
    if request.method == 'POST':
        form = DetallePedidoForm(request.POST)
        if form.is_valid():
            plato = get_object_or_404(Plato, id_plato=form.cleaned_data['id_plato'])
            pedido = get_object_or_404(Pedido, id_pedido=form.cleaned_data['id_pedido'])
            
            # Verificar si ya existe este detalle
            detalle_existente = DetallePedido.objects.filter(
                id_plato=plato, 
                id_pedido=pedido
            ).first()
            
            if detalle_existente:
                # Si existe, actualizar en lugar de crear
                detalle_existente.cantidad = form.cleaned_data['cantidad']
                detalle_existente.subtotal = form.cleaned_data['subtotal']
                detalle_existente.save()
            else:
                # Si no existe, crear nuevo
                DetallePedido.objects.create(
                    id_plato=plato,
                    id_pedido=pedido,
                    cantidad=form.cleaned_data['cantidad'],
                    subtotal=form.cleaned_data['subtotal']
                )
            return redirect('listar_detalles_pedido')
    else:
        form = DetallePedidoForm()
    return render(request, 'nuevo_detalle_pedido.html', {'form': form})

def eliminar_detalle_pedido(request, id_plato, id_pedido):
    detalle = get_object_or_404(
        DetallePedido, 
        id_plato=id_plato, 
        id_pedido=id_pedido
    )
    detalle.delete()
    return redirect('listar_detalles_pedido')

def index(request):
    return render(request, 'index.html')