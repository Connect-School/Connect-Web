from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.contrib.auth.models import User
from core.serializers import UserSerializer, UsuarioPolySerializer, OrganizacaoPolySerializer
from core.models import Usuario, Organizacao


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioPolySerializer


class OrganizacaoViewSet(ModelViewSet):
    queryset = Organizacao.objects.all()
    serializer_class = OrganizacaoPolySerializer
