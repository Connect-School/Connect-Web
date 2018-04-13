from django.contrib import admin
from responsabilidade.models import *

# Register your models here.
admin.site.register(Dependente)
admin.site.register(Responsavel)

admin.site.register(PaiResponsavel)
admin.site.register(AlunoDependente)


admin.site.register(EscolaResponsavel)
admin.site.register(EscolaDependente)

admin.site.register(ProfessorDependente)


