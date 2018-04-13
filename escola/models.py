from django.db import models
from core.models import Usuario, Organizacao
from responsabilidade.models import EscolaResponsavel, EscolaDependente, ProfessorDependente


class Escola(Organizacao):
    perfil_responsavel = models.OneToOneField(EscolaResponsavel, related_name="escola", null=True, blank=True, on_delete=models.PROTECT)
    perfil_dependente = models.OneToOneField(EscolaDependente, related_name="escola", null=True, blank=True, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=16)

    def get_name(self):
        return self.nome

    def __str__(self):
        return self.get_name()


class GerenteEscola(Usuario):
    escola = models.ForeignKey(Escola, related_name="gerentes", null=True, blank=True, on_delete=models.PROTECT)


class Professor(Usuario):
    perfil_dependente = models.OneToOneField(ProfessorDependente, related_name="professor", null=True, blank=True, on_delete=models.PROTECT)
