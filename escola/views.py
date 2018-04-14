from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated

    return render(request, 'escola/index.html', context)
