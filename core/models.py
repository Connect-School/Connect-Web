from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

# Create your models here.
class Dependente(models.Model):
    pass


class Responsavel(models.Model):
    pass


class Organizacao(PolymorphicModel):
    pass


class Usuario(PolymorphicModel):
    perfil_user = models.OneToOneField(User, on_delete=models.PROTECT)


class Pai(Usuario):
    pass


class Aluno(Usuario):
    pass
