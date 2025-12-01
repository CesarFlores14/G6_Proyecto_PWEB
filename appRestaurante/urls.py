from django.urls import path
from . import views
urlpatterns = [
    # URLs para Plato
    path('platos/', views.listar_platos, name='listar_platos'),
    path('platos/nuevo/', views.crear_plato, name='crear_plato'),
    path('platos/actualizar/<int:id>/', views.actualizar_plato, name='actualizar_plato'),
    path('platos/eliminar/<int:id>/', views.eliminar_plato, name='eliminar_plato'),
    
    # URLs para Mesa
    path('mesas/', views.listar_mesas, name='listar_mesas'),
    path('mesas/nuevo/', views.crear_mesa, name='crear_mesa'),
    path('mesas/actualizar/<int:id>/', views.actualizar_mesa, name='actualizar_mesa'),
    path('mesas/eliminar/<int:id>/', views.eliminar_mesa, name='eliminar_mesa'),
    
    # URLs para Pedido
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/nuevo/', views.crear_pedido, name='crear_pedido'),
    path('pedidos/actualizar/<int:id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/eliminar/<int:id>/', views.eliminar_pedido, name='eliminar_pedido'),
    
    # URLs para DetallePedido (CORREGIDAS)
    path('detalles-pedido/', views.listar_detalles_pedido, name='listar_detalles_pedido'),
    path('detalles-pedido/nuevo/', views.crear_detalle_pedido, name='crear_detalle_pedido'),
    path('detalles-pedido/eliminar/<int:id_plato>/<int:id_pedido>/', views.eliminar_detalle_pedido, name='eliminar_detalle_pedido'),
    
    # Página principal
    path('', views.index, name='index'),
]