from django.shortcuts import render
from django.utils import timezone
from .models import Profesor
# Create your views here.
def listado (request):
    profesores = Profesor.objects.all()
    return render(request,'luma/listado.html',{'profesores': profesores})
