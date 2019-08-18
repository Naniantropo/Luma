from django.db import models
from django.utils import timezone


class Profesor(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    centro = models.CharField(max_length=200)
   #asignatura = models.ForeignKey('asignatura.id'),on_delete=models.CASCADE)
   #libro = models.ForeignKey('libro.id'),on_delete=models.CASCADE)

    def publish(self):
        self.curso

    