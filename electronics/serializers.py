from rest_framework import serializers

from electronics.models import Product, Link


class ProductSerializers(serializers.ModelSerializer):
    """ Сериализатор для модели продукта """

    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializers(serializers.ModelSerializer):
    """ Сериализатор для модели звена сети """

    class Meta:
        model = Link
        fields = '__all__'
