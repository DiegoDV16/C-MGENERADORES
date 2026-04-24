from django.db import models


# 🔹 ROLES
class Rol(models.Model):
    rol = models.CharField(max_length=25)

    def __str__(self):
        return self.rol


# 🔹 MODELOS_GENERADORES
class ModeloGenerador(models.Model):
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.modelo
# * MARCA_GENERADOR
class MarcaGenerador(models.Model):
    marca = models.CharField(max_length=25)

    def __str__(self):
        return self.marca
# 🔹 USUARIOS
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# 🔹 TIPO USO GENERADORES
class TipoUsoGenerador(models.Model):
    tipo = models.CharField(max_length=25)

    def __str__(self):
        return self.tipo


# 🔹 GENERADORES
class Generador(models.Model):
    tipo_uso = models.ForeignKey(TipoUsoGenerador, on_delete=models.CASCADE)
    generador = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=25)
    numero_serie = models.CharField(max_length=100)

    def __str__(self):
        return self.generador


# 🔹 COMPONENTES
class Componente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# 🔹 RELACIÓN GENERADOR - COMPONENTES
class ComponenteGenerador(models.Model):
    generador = models.ForeignKey(Generador, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    horometro = models.IntegerField()
    fecha_ultimo_mantenimiento = models.DateField()

    def __str__(self):
        return f"{self.generador} - {self.componente}"


# 🔹 MANTENIMIENTO
class MantenimientoGenerador(models.Model):
    generador = models.ForeignKey(Generador, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.generador} - {self.fecha}"


# 🔹 DETALLE MANTENIMIENTO
class DetalleMantenimiento(models.Model):
    mantenimiento = models.ForeignKey(MantenimientoGenerador, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    horometro = models.IntegerField()
    foto = models.ImageField(upload_to='evidencias/', null=True, blank=True)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.mantenimiento} - {self.componente}"