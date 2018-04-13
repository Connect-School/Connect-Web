from django.db import models
from polymorphic.models import PolymorphicModel


class Responsavel(PolymorphicModel):
    poly_type = models.CharField(max_length=40)

    # def get_name(self):
    #     return eval("self.{}.get_name()".format(self.poly_type))

    # def __str__(self):
    #     return self.get_name()

class PaiResponsavel(Responsavel):

    def __str__(self):
        return self.pai.get_name()

class EscolaResponsavel(Responsavel):

    def __str__(self):
        return self.escola.get_name()

class Dependente(PolymorphicModel):
    poly_type = models.CharField(max_length=40)
    responsavel = models.ForeignKey(Responsavel, related_name="dependentes", null=True, blank=True, on_delete=models.PROTECT)

    # def get_name(self):
    #     return eval("self.{}.get_name()".format(self.poly_type))
    #
    # def __str__(self):
    #     return self.get_name()

class EscolaDependente(Dependente):

    def __str__(self):
        return self.escola.get_name()

class ProfessorDependente(Dependente):

    def __str__(self):
        return self.professor.get_name()

class AlunoDependente(Dependente):

    def __str__(self):
        return self.aluno.get_name()
