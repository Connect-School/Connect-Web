from django.db import models
from core.models import Organizacao, Usuario
from responsabilidade.models import SecretariaResponsavel, SecretariaDependente

# Create your models here.
class Secretaria(Organizacao):
    perfil_responsavel = models.OneToOneField(SecretariaResponsavel, related_name="secretaria", null=True, blank=True, on_delete=models.PROTECT)
    perfil_dependente = models.OneToOneField(SecretariaDependente, related_name="secretaria", null=True, blank=True, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=16)

    def get_name(self):
        return self.nome

    def __str__(self):
        return self.get_name()

class GerenteSecretaria(Usuario):
    secretaria = models.ForeignKey(Secretaria, related_name="gerentes", null=True, blank=True, on_delete=models.PROTECT)
