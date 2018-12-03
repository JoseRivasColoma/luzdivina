from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('bacan/', views.VariableBase, name='base'),
    path('ingreso_personas/', views.IngresoPersonas, name='ingreso_personas'),
    path('listado_personas/', views.ListadoPersonas, name='listado_personas'),
    path('eliminar_persona/<id>/', views.Eliminar_Personas, name='eliminar_persona'),
    path('modificar_persona/<id>/', views.ModificacionPersonas, name='modificar_persona'),
    path('lista_filtro_cargo/<id>/', views.ListadoPersonasFiltroTipoPersona, name='lista_filtro_cargo'),

]