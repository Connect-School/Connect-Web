from django.db import models
from django.contrib.auth.models import User
from responsabilidade.models import PaiResponsavel, AlunoDependente
from polymorphic.models import PolymorphicModel

# Create your models here.
class Organizacao(PolymorphicModel):
    pass


class Usuario(PolymorphicModel):
    perfil_user = models.OneToOneField(User, on_delete=models.PROTECT)

    def get_name(self):
        return self.perfil_user.username

    def __str__(self):
        return self.get_name()


class Pai(Usuario):
    perfil_responsavel = models.OneToOneField(PaiResponsavel, related_name="pai", null=True, blank=True, on_delete=models.PROTECT)


class Aluno(Usuario):
    perfil_dependente = models.OneToOneField(AlunoDependente, related_name="aluno", null=True, blank=True, on_delete=models.PROTECT)
