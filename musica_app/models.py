from django.db import models

# Create your models here.
class Musico(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    instrumento_principal = models.CharField(null=True, max_length=100)

class Album(models.Model):
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    estrellas = models.IntegerField()

# CMD :  python manage.py makemigrations musica_app
