from rest_framework import serializers   # type: ignore

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

    def update(self, instance, validated_data):
        """ запретит на обновление через API поля Задолженность """
        if 'debt' in validated_data:
            validated_data.pop('debt')
        return super().update(instance, validated_data)
