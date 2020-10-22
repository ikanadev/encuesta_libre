from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Pregunta, Opcion
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'encuesta/index.html'

    def get_queryset(self):
        return Pregunta.objects.order_by('-fecha')


class ResultsView(generic.DetailView):
    model = Pregunta
    template_name = 'encuesta/resultados.html'


class QuestionFormView(generic.TemplateView):
    template_name = 'encuesta/nuevaPregunta.html'


def nuevaPregunta(request):
    texto_pregunta = request.POST['texto_pregunta']
    nro_opciones = int(request.POST['nro_opciones'])
    opciones = []
    for i in range(nro_opciones):
        opciones.append(request.POST['opcion_'+str(i+1)])
    pregunta = Pregunta(pregunta=texto_pregunta)
    pregunta.save()
    for opcion in opciones:
        opt = Opcion(texto=opcion, pregunta=pregunta)
        opt.save()
    return redirect('encuesta:index')


def nuevoVoto(request, id_pregunta):
    pregunta = get_object_or_404(Pregunta, pk=id_pregunta)
    print(request.POST['opcion'])
    opcion = pregunta.opcion_set.get(pk=request.POST['opcion'])
    opcion.votos += 1
    opcion.save()
    return redirect('encuesta:index')
