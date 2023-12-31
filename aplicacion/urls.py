from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('cursos/', cursos, name="cursos"),
    path('entregables/', entregables, name="entregables"),

    path('curso_form/', cursoForm, name="curso_form"),
    path('curso_form2/', cursoForm2, name="curso_form2"),

    path('buscar_comision/', buscarComision, name="buscar_comision"),
    path('buscar2/', buscar2, name="buscar2"),
]
