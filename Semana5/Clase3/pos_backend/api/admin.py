from django.contrib import admin

from .models import Categoria, Pedido, PedidoPlato,Plato,Mesa
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Plato)
admin.site.register(Mesa)
admin.site.register(Pedido)
admin.site.register(PedidoPlato)