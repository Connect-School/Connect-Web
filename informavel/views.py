from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Gerente
from .models import Notificacao, Bullying, InformavelForum


@login_required
def detalhar_forum(request, id_informavel):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated
    usuario = get_object_or_404(Gerente, perfil_user=request.user)
    isinstance(usuario, Gerente)
    context['organizacao'] = usuario.get_organizacao()
    context['tipo_organizacao'] = usuario.get_organizacao().get_tipo()

    forum = get_object_or_404(InformavelForum, pk=id_informavel)

    context['forum'] = forum
    context['variar'] = True

    return render(request, 'informavel/detalhar_forum.html', context)


@login_required
def detalhar_aviso(request, id_notificacao):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated
    usuario = get_object_or_404(Gerente, perfil_user=request.user)
    isinstance(usuario, Gerente)
    context['organizacao'] = usuario.get_organizacao()
    context['tipo_organizacao'] = usuario.get_organizacao().get_tipo()

    notificacao = get_object_or_404(Notificacao, pk=id_notificacao)
    notificacao.read = True
    notificacao.save()

    context['aviso'] = notificacao.aviso

    return render(request, 'informavel/detalhar_aviso.html', context)


@login_required
def detalhar_bullying(request, id_informavel):
    context = {}
    context['usuario_autenticado'] = request.user.is_authenticated
    usuario = get_object_or_404(Gerente, perfil_user=request.user)
    isinstance(usuario, Gerente)
    context['organizacao'] = usuario.get_organizacao()
    context['tipo_organizacao'] = usuario.get_organizacao().get_tipo()

    bullying = get_object_or_404(Bullying, pk=id_informavel)
    bullying.read = True
    bullying.save()

    context['bullying'] = bullying

    return render(request, 'informavel/detalhar_bullying.html', context)
