from django.contrib import admin
from core.models import Usuario, Pai, Aluno, Dependente, Responsavel

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Pai)
admin.site.register(Aluno)

admin.site.register(Dependente)
admin.site.register(Responsavel)
