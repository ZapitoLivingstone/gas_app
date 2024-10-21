from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ingresar_solicitud/', views.ingresar_solicitud, name='ingresar_solicitud'),
    path('administrar_solicitudes/', views.administrar_solicitudes, name='administrar_solicitudes'),
    path('detalle_solicitud/<int:pk>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('cambiar_estado/<int:pk>/', views.cambiar_estado, name='cambiar_estado'),
    path('eliminar_solicitud/<int:pk>/', views.eliminar_solicitud, name='eliminar_solicitud'),
    path('buscar_solicitud/', views.buscar_solicitud, name='buscar_solicitud'),
]