from django.db import models
from polymorphic.models import PolymorphicModel
from core.models import Usuario, Organizacao
from responsabilidade.models import Responsavel
from model_utils import Choices


class Mensagem(PolymorphicModel):
    texto = models.CharField(max_length=255)
    data = models.DateTimeField()

    def __str__(self):
        return "Mensagem ({})".format(self.pk)


class MensagemIdentificada(Mensagem):
    criador = models.ForeignKey(Usuario, related_name="mensagens_identificadas", on_delete=models.CASCADE)

    def __str__(self):
        return "Mensagem ({}) de {}".format(self.pk, self.criador.get_name())


class Informavel(PolymorphicModel):

    def __str__(self):
        return "Informavel ({})".format(self.pk,)


class Aviso(Informavel):
    mensagem = models.OneToOneField(MensagemIdentificada, related_name="aviso", null=True, blank=True,
                                    on_delete=models.PROTECT)

    def __str__(self):
        return "Aviso ({}) de {}".format(self.pk, self.mensagem.criador.get_name())


class Notificacao(models.Model):
    usuarios = models.ManyToManyField(Usuario, related_name='notificacoes', through='UsuarioNotificacao')
    aviso = models.OneToOneField(MensagemIdentificada, related_name="notificacao", null=True, blank=True, on_delete=models.PROTECT)


class UsuarioNotificacao(models.Model):
    class Meta:
        db_table = 'users_notifications'
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    notificacao = models.ForeignKey(Notificacao, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)


class InformavelResolvivel(Informavel):
    encarregado = models.ForeignKey(Usuario, related_name="resolviveis", null=True, blank=True,
                                    on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    @property
    def is_bullying(self):
        if isinstance(self, Bullying):
            return True
        return False

    def __str__(self):
        return "Informavel resolvivel ({})".format(self.pk)


class Bullying(InformavelResolvivel):

    mensagem = models.OneToOneField(Mensagem, related_name="bullying", null=True, blank=True, on_delete=models.PROTECT)
    # TODO AssuntoUsuario (?)


    def __str__(self):
        return "Mensagem anônima ({}) para {}".format(self.pk, self.responsavel.get_name())


class InformavelForum(InformavelResolvivel):
    TIPO = Choices(('reclamacao', ('Reclamação')), ('sugestao', ('Sugestão')), ('solicitacao', ('Solicitação')))
    tipo = models.CharField(choices=TIPO, default=TIPO.reclamacao, max_length=11)

    def __str__(self):
        return "Forum ({})".format(self.pk)


class MensagemForum(MensagemIdentificada):
    forum = models.ForeignKey(InformavelForum, related_name="mensagens", on_delete=models.CASCADE)

    def __str__(self):
        return "Mensagem ({}) de {} para forum ({})".format(self.pk, self.criador.get_name(), self.forum.pk)


class InformavelForumOrganizacao(InformavelForum):
    assunto = models.ForeignKey(Organizacao, on_delete=models.CASCADE)


class InformavelForumUsuario(InformavelForum):
    assunto = models.ForeignKey(Usuario, on_delete=models.CASCADE)
