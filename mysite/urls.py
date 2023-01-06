from django.urls import path
from .views import index, sobre, participantes, participante, error404, error500

from django.conf.urls import handler404, handler500

handler404 = error404
handler500 = error500

urlpatterns = [
    path('', index, name='index'),
    path('sobre', sobre, name='sobre'),
    path('participantes', participantes, name='participantes'),
    path('participante/<int:pk>', participante, name='participante')

]
