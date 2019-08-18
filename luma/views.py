from django.shortcuts import render
from django.utils import timezone
from .models import Profesor, Alumno
# Create your views here.
def listado_profesor(request):
    profesores = Profesor.objects.all()
    return render(request, 'luma/listado.html',{'profesores': profesores})
def listado_alumnos (request):
    alumnos = Alumno.objects.all()
    return render(request, 'luma/listado_alumnos.html', {'alumnos': alumnos})