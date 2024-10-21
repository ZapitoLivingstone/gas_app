from django.shortcuts import render, redirect, get_object_or_404
from .models import Solicitud
from .forms import SolicitudForm
from datetime import datetime
from django.utils import timezone

def index(request):
    return render(request, 'index.html')

def ingresar_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('administrar_solicitudes')
    else:
        form = SolicitudForm()
    return render(request, 'ingresar_solicitud.html', {'form': form})

def administrar_solicitudes(request):
    solicitudes = Solicitud.objects.all()  
    for solicitud in solicitudes:
        solicitud.actualizar_estado() 
    return render(request, 'administrar_solicitudes.html', {'solicitudes': solicitudes})

def detalle_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk) 
    solicitud.actualizar_estado()  
    return render(request, 'detalle_solicitud.html', {'solicitud': solicitud})

def cambiar_estado(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in dict(Solicitud.ESTADOS):
            solicitud.estado = nuevo_estado
            if nuevo_estado == 'A':
                solicitud.fecha_aceptacion = timezone.now() 
            solicitud.save()  
        return redirect('administrar_solicitudes')
    return render(request, 'cambiar_estado.html', {'solicitud': solicitud})

def eliminar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)  
    if request.method == 'POST':
        solicitud.delete() 
        return redirect('administrar_solicitudes')
    return render(request, 'eliminar_solicitud.html', {'solicitud': solicitud})

def buscar_solicitud(request):
    solicitud = None
    if request.method == 'GET':
        rut = request.GET.get('rut')
        if rut:
            solicitud = Solicitud.objects.filter(rut=rut).first()  
    return render(request, 'buscar_solicitud.html', {'solicitud': solicitud})
