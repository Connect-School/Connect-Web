from django.db import models
from polymorphic.models import PolymorphicModel


class Assunto(PolymorphicModel):
    pass


class AssuntoUsuario(Assunto):
    pass


class AssuntoOrganizacao(Assunto):
    pass


class Informavel(PolymorphicModel):
    pass


class InformavelUnico(Informavel):
    pass


class Bullying(InformavelUnico):
    pass


class Aviso(InformavelUnico):
    pass


class InformavelForum(Informavel):
    pass


class Reclamacao(InformavelForum):
    pass


class Sugestao(InformavelForum):
    pass


class Solicitacao(InformavelForum):
    pass
