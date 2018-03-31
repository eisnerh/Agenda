from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Evento
from .forms import EntryForm
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    eventos = Evento.objects.all()[:10]

    context = {
        'NombreEvento': 'List of Events',
        'CodigoEvento': eventos
    }

    return render(request, 'agenda_eventos/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/calendar')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


class IndexTemplateView(TemplateView):
    template_name = 'agenda_eventos/index.html'
