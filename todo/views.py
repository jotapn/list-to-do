from rest_framework import viewsets
from .serializer import UsuarioSerializer, CardSerializer
from .models import Usuario, Card


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
