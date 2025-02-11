from django.db import models


# Tabla Estructuras
class Estructura(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    fecha_instalacion = models.DateField()
    foto = models.ImageField(upload_to='estructuras_fotos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

# Tabla Trabajos
class Trabajo(models.Model):
    estructura = models.ForeignKey(Estructura, on_delete=models.CASCADE, related_name='trabajos')
    descripcion = models.TextField()
    fecha_programada = models.DateField()
    fecha_ejecucion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('realizado', 'Realizado')], default='pendiente')
    documentos = models.FileField(upload_to='trabajos_documentos/', null=True, blank=True)

    def __str__(self):
        return f"Trabajo en {self.estructura.nombre} - {self.estado}"

# Tabla Encargados
class Encargado(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=20)
    puesto = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='encargados_fotos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

# Tabla Planes de Mantenimiento
class PlanMantenimiento(models.Model):
    estructura = models.ForeignKey(Estructura, on_delete=models.CASCADE, related_name='planes_mantenimiento')
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, related_name='planes_mantenimiento')
    encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE, related_name='planes_mantenimiento')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo = models.CharField(max_length=50, choices=[('preventivo', 'Preventivo'), ('correctivo', 'Correctivo')])
    documentos = models.FileField(upload_to='planes_mantenimiento_documentos/', null=True, blank=True)

    def __str__(self):
        return f"Plan de Mantenimiento para {self.estructura.nombre} - {self.tipo}"
