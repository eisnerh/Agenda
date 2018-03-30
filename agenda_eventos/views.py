from django.shortcuts import render
from .models import Evento

# Create your views here.
def index(request):
    # return HttpResponse('Hello from POSTS')

    posts = Evento.objects.all()[:10]

    context = {
        'title': 'NombreEvento',
        'CodigoEvento': 'CodigoEvento'
    }

    return render(request, 'agenda_eventos/index.html', context)
