from django.urls import path

from . import views

urlpatterns = [
    path('detalhar/forum/<id_informavel>', views.detalhar_forum, name='detalhar_forum'),
    path('detalhar/aviso/<id_notificacao>', views.detalhar_aviso, name='detalhar_aviso'),
    path('detalhar/bullying/<id_informavel>', views.detalhar_bullying, name='detalhar_bullying'),
]