from django.shortcuts import render
from agenda_App.models import Evento

# Create your views here.
def agenda(request):
    evento = Evento.objects.all()
    response = {'evento': evento}
    return render(request, 'agenda.html', response)