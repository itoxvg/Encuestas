from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from encuestas.models import Encuesta, Eleccion

def index(request):
	lista_encuestas = Encuesta.objects.all().order_by('-fecha_pub')[:5]
	context = { 'lista_encuestas': lista_encuestas}
	return render(request, 'encuestas/index.html', context)

def detalles(request, id_encuesta):
	encuesta = get_object_or_404(Encuesta,pk = id_encuesta)
	return render(request, 'encuestas/detalles.html', {'encuesta':encuesta})

def votos(request, id_encuesta):
    p = get_object_or_404(Encuesta, pk= id_encuesta)
    try:
        opcion_seleccionada = p.eleccion_set.get(pk=request.POST['eleccion'])
    except (KeyError, Eleccion.DoesNotExist):
        return render(request, 'encuestas/detalles.html', {
            'encuesta': p,
            'error_message': 'No ha seleccionado una opcion.',
        })
    else:
        opcion_seleccionada.votos += 1
        opcion_seleccionada.save()
        return HttpResponseRedirect(reverse('encuestas:resultados', args=(p.id,)))

def resultados(request, id_encuesta):
	return HttpResponse("tus resutaldos de encuesta %s." %id_encuesta)

def resultados(request, id_encuesta):
    encuesta = get_object_or_404(Encuesta, pk=id_encuesta)
    return render(request, 'encuestas/resultados.html',{'encuesta':encuesta})