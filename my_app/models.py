from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TIPOS_DE_USUARIO = (
        ("ALUMNO", "Alumno"),
        ("MAESTRO", "Maestro"),
        ("ADMINISTRATIVO", "Administrativo"),
    )
    tipo_de_usuario = models.CharField(max_length=20, choices=TIPOS_DE_USUARIO)


class Alumno(Profile):
    pass


class Maestro(Profile):
    pass


class Administrativo(Profile):
    pass


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    nota = models.FloatField(null=True, blank=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    fecha_baja = models.DateTimeField(null=True, blank=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
