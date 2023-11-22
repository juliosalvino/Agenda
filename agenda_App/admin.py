from django.contrib import admin
from agenda_App.models import Evento
# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo', 'usuario', 'data_evento')

admin.site.register(Evento, EventoAdmin)

