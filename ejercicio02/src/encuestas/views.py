from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from encuestas.models import Eleccion, Encuesta

class IndexView(generic.ListView):
    template_name = 'encuestas/index.html'
    context_object_name = 'lista_encuestas'

    def get_queryset(self):
        """Return the last five published polls."""
        return Encuesta.objects.order_by('-fecha_pub')[:5]


class DetailView(generic.DetailView):
    model = Encuesta
    template_name = 'encuestas/detalles.html'


class ResultsView(generic.DetailView):
    model = Encuesta
    template_name = 'encuestas/resultados.html'

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

