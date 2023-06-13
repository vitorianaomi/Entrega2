from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    context = {'mensagem': "Olá! Aqui você encontra a página principal do site IFRN Campus Pau dos Ferros."}
    return render(request, 'curso/index.html', context)

def detalhe_curso(request, id_curso):
    curso = get_object_or_404(Curso, id = id_curso)
    context = {'objeto' : curso}
    return render(request,'curso/detalhecurso.html',context)

def lista_cursos(request):
    cursos = Curso.objects.all()
    context = {'lista_cursos' : cursos} 
    return render(request,'curso/cursos.html',context)

def sobre(request):
    context = {'descrição': "Olá! Aqui você encontra algumas informações sobre quem sou eu."}
    return render(request, 'curso/sobre.html', context)
