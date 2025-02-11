from django.contrib import admin

from Aplicaciones.pro6.models import Encargado, Estructura, PlanMantenimiento, Trabajo

# Register your models here.
admin.site.register(Estructura)
admin.site.register(Trabajo)
admin.site.register(Encargado)
admin.site.register(PlanMantenimiento)
