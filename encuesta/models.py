import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pregunta

    def publicado_hoy(self):
        return self.fecha >= timezone.now() - datetime.timedelta(days=1)
    publicado_hoy.admin_order_field = 'fecha'
    publicado_hoy.boolean = True
    publicado_hoy.short_description = 'Publicado hoy?'


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.pregunta

