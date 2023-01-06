from django.contrib import admin
from .models import Participantes

class ParticipantesAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'filme_favorito', 'idade', 'cidade', 'estado')

admin.site.register(Participantes)


