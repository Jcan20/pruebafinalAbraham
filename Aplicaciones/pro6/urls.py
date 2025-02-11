from django.urls import path
from . import views  # Asegúrate de que views.py también existe

urlpatterns = [
    # Rutas existentes
    path('', views.home, name='home'),

    path('exportar/excel/', views.exportarTrabajosExcel, name='exportar_trabajos_excel'),
    path('exportar/csv/', views.exportarTrabajosCSV, name='exportar_trabajos_csv'),
    path('exportar/pdf/', views.exportarTrabajosPDF, name='exportar_trabajos_pdf'),

 
    path('listadoEncargados/', views.listadoEncargados, name='listado_encargados'),
    path('nuevoEncargado/', views.nuevoEncargado, name='nuevoEncargado'),
    path('guardarEncargado/', views.guardarEncargado, name='guardarEncargado'),
    path('editarEncargado/<int:id>/', views.editarEncargado, name='editarEncargado'),
    path('procesoActualizarEncargado/', views.procesoActualizarEncargado, name='procesoActualizarEncargado'),
    path('eliminarEncargado/<int:id>/', views.eliminarEncargado, name='eliminarEncargado'),

    # Estructura
    path('listadoEstructuras/', views.listadoEstructuras, name='listado_estructuras'),
    path('nuevaEstructura/', views.nuevaEstructura, name='nuevaEstructura'),
    path('guardarEstructura/', views.guardarEstructura, name='guardarEstructura'),
    path('editarEstructura/<int:id>/', views.editarEstructura, name='editarEstructura'),
    path('procesoActualizarEstructura/', views.procesoActualizarEstructura, name='procesoActualizarEstructura'),
    path('eliminarEstructura/<int:id>/', views.eliminarEstructura, name='eliminarEstructura'),


# Exportaciones
path('exportar_estructuras_excel/', views.exportarEstructurasExcel, name='exportar_estructuras_excel'),
path('exportar_estructuras_csv/', views.exportarEstructurasCSV, name='exportar_estructuras_csv'),
path('exportar_estructuras_pdf/', views.exportarEstructurasPDF, name='exportar_estructuras_pdf'),



    # Trabajo
    path('listadoTrabajos/', views.listadoTrabajos, name='listado_trabajos'),
    path('nuevoTrabajo/', views.nuevoTrabajo, name='nuevoTrabajo'),
    path('guardarTrabajo/', views.guardarTrabajo, name='guardarTrabajo'),
    path('editarTrabajo/<int:id>/', views.editarTrabajo, name='editarTrabajo'),
    path('procesoActualizarTrabajo/', views.procesoActualizarTrabajo, name='procesoActualizarTrabajo'),
    path('eliminarTrabajo/<int:id>/', views.eliminarTrabajo, name='eliminarTrabajo'),

path('listado-planes-mantenimiento/', views.listado_planes_mantenimiento, name='listado_planes_mantenimiento'),
    path('nueva-plan/', views.nuevaPlanMantenimiento, name='nueva_plan_mantenimiento'),
    path('guardar-plan-mantenimiento/', views.guardarPlanMantenimiento, name='guardar_plan_mantenimiento'),
    path('editar-plan-mantenimiento/<int:id>/', views.editarPlanMantenimiento, name='editar_plan_mantenimiento'),
    path('eliminar-plan-mantenimiento/<int:id>/', views.eliminarPlanMantenimiento, name='eliminar_plan_mantenimiento'),
path('proceso-actualizar-plan/', views.procesoActualizarPlanMantenimiento, name='procesoActualizarPlanMantenimiento'),

path('exportar-plan-excel/', views.exportarPlanesExcel, name='exportar_planes_excel'),
 path('exportar-plan-csv/', views.exportarPlanesCSV, name='exportar_planes_csv'),
path('exportar-plan-pdf/', views.exportarPlanesPDF, name='exportar_planes_pdf'),

path('enviar-correo-encargado/<int:id>/', views.enviar_correo_encargado, name='enviarCorreoEncargado'),

]

