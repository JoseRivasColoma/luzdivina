from django.shortcuts import render, redirect
from .models import Comunidad, TipoPersona, TipoEvento, Persona
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request, 'core/home.html')


def ListadoPersonas(request):
    personas = Persona.objects.all()
    return render(request, 'core/listado_personas.html',{'personas':personas})

def VariableBase(request):
    tipos_persona = TipoPersona.objects.all()
    variables = {
        'tp':tipos_persona
    }

    return render(request, 'core/base.html', variables)

def ListadoPersonasFiltroTipoPersona(request, id):
    tipos_persona = TipoPersona.objects.all()
    variables = {
        'tp':tipos_persona
    }

    return render(request, 'core/base.html', variables)

def Eliminar_Personas(request, id):
    #buscar la persona
    persona = Persona.objects.get(id=id)

    try:
        persona.delete()
        mensaje = "Fiel eliminado :("
        messages.success(request, mensaje)
    except:
        mensaje = "Fiel No eliminado, suerte para la próxima Dios ;)"
        messages.error(request, mensaje)
    return redirect('listado_personas')

def IngresoPersonas(request):
    tipos_persona = TipoPersona.objects.all()
    tipos_evento = TipoEvento.objects.all()
    comunidades = Comunidad.objects.all()

    variables = {
        'tipos_persona':tipos_persona,
        'tipos_evento':tipos_evento,
        'comunidades':comunidades
    }

    if request.POST:
        persona = Persona()

        persona.apellido = request.POST.get('txtApellido')
        persona.nombre = request.POST.get('txtNombre')
        persona.edad = request.POST.get('txtEdad')
        persona.sexo = request.POST.get('rbSexo')
        persona.telefono = request.POST.get('txtTelefono')
        persona.direccion = request.POST.get('txtDireccion')
        tipo_persona = TipoPersona()
        tipo_evento = TipoEvento()
        comunidad = Comunidad()
        tipo_persona.id = request.POST.get('cboCargo')
        tipo_evento.id = request.POST.get('cboEventos')
        comunidad.id = request.POST.get('cboComunidad')

        persona.tipo_persona = tipo_persona
        persona.tipo_evento = tipo_evento
        persona.comunidad = comunidad
        
        try:
            persona.save()
            variables['mensaje'] = "Fiel Agregado"
        except:
            variables['mensaje'] = "Fiel No Agregado :(, Satán estaría orgulloso de ti"
        
        
    return render (request, 'core/ingreso_personas.html',variables)
    
def ModificacionPersonas(request, id):
    persona =Persona.objects.get(id=id)
    tipos_persona = TipoPersona.objects.all()
    tipos_evento = TipoEvento.objects.all()
    comunidades = Comunidad.objects.all()

    if request.POST:
        persona = Persona()
        persona.id = request.POST.get('txtId')
        persona.apellido = request.POST.get('txtApellido')
        persona.nombre = request.POST.get('txtNombre')
        persona.edad = request.POST.get('txtEdad')
        persona.sexo = request.POST.get('rbSexo')
        persona.telefono = request.POST.get('txtTelefono')
        persona.direccion = request.POST.get('txtDireccion')
        tipo_persona = TipoPersona()
        tipo_evento = TipoEvento()
        comunidad = Comunidad()
        tipo_persona.id = request.POST.get('cboCargo')
        tipo_evento.id = request.POST.get('cboEventos')
        comunidad.id = request.POST.get('cboComunidad')

        persona.tipo_persona = tipo_persona
        persona.tipo_evento = tipo_evento
        persona.comunidad = comunidad
        
        try:
            persona.save()
            messages.success(request, "Fiel Modificado")
        except:
            messages.error(request, "Fiel no ha podido modificarse")
        return redirect('listado_personas')
    variables = {
        'persona': persona,
        'tipos_persona':tipos_persona,
        'tipos_evento':tipos_evento,
        'comunidades':comunidades
    }

    return render(request, 'core/modificar_persona.html', variables)