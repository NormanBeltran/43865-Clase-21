from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def profesores(request):
    return render(request, "aplicacion/profesores.html")

def estudiantes(request):
    return render(request, "aplicacion/estudiantes.html")

def entregables(request):
    return render(request, "aplicacion/entregables.html")

def cursos(request):
    ctx = {"cursos": Curso.objects.all() }
    return render(request, "aplicacion/cursos.html", ctx)

def cursoForm(request):
    if request.method == "POST":                
        curso = Curso(nombre=request.POST['nombre'], comision=request.POST['comision'])
        curso.save()
        return HttpResponse("Se grabo con exito el curso!")
    
    return render(request, "aplicacion/cursoForm.html")

def cursoForm2(request):
    if request.method == "POST":   
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data.get('nombre')
            curso_comision = miForm.cleaned_data.get('comision')
            curso = Curso(nombre=curso_nombre, comision=curso_comision)
            curso.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = CursoForm()

    return render(request, "aplicacion/cursoForm2.html", {"form":miForm})

def buscarComision(request):
    return render(request, "aplicacion/buscarComision.html")

def buscar2(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, 
                      "aplicacion/resultadosComision.html", 
                      {"comision": comision, "cursos":cursos})
    return HttpResponse("No se ingresaron datos para buscar!")
