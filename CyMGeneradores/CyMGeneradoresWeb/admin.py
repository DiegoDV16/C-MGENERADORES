from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(TipoUsoGenerador)
admin.site.register(Generador)
admin.site.register(Componente)
admin.site.register(ComponenteGenerador)
admin.site.register(MantenimientoGenerador)
admin.site.register(DetalleMantenimiento)