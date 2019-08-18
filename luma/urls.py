from django.urls import path
from . import views

urlpatterns = [
        path('profesores', views.listado_profesor, name='listado_profesores'),
        path('alumnos', views.listado_alumnos, name= 'listado_alumnos')
        ]
