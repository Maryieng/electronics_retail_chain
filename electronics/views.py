from django_filters.rest_framework import DjangoFilterBackend   # type: ignore
from rest_framework import viewsets   # type: ignore
from rest_framework.permissions import IsAuthenticated   # type: ignore

from electronics.filter import LinkFilter
from electronics.models import Product, Link
from electronics.serializers import ProductSerializers, LinkSerializers


class ProductViewSet(viewsets.ModelViewSet):
    """ CRUD модели продукта """
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class LinkViewSet(viewsets.ModelViewSet):
    """ CRUD модели звена сети """
    serializer_class = LinkSerializers
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LinkFilter
