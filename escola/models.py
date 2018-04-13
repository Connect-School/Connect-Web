from django.db import models
from core.models import Usuario, Responsavel, Dependente, Organizacao



class Escola(Organizacao):
    pass


class GerenteEscola(Usuario):
    pass
