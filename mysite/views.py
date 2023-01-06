from django.shortcuts import render, get_object_or_404
from .models import Participantes


def index(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')


def participantes(request):
    participantes = Participantes.objects.all()
    context = {
        'participantes': participantes
    }
    return render(request, 'participantes.html', context)


def participante(request, pk):
    print(f'Pk: {pk}')
    part = get_object_or_404(Participantes, id=pk)
    context = {
        'participantes': part
    }
    return render(request, 'participante.html', context)

def error404(request, exception):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')
