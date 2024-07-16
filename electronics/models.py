from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    model = models.CharField(max_length=150, verbose_name='Модель')
    create_data = models.DateField(verbose_name='Дата выхода на рынок')

    def __str__(self) -> str:
        return f'{self.name} {self.model}'

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"


class Link(models.Model):
    """ Модель звена сети """

    HIERARCHICAL_LEVEL = [
        (0, 'Завод'),
        (1, 'Магазин'),
        (2, 'Индивидуальный предприниматель')]

    type_level = models.PositiveIntegerField(choices=HIERARCHICAL_LEVEL, verbose_name='Тип')
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=100, verbose_name='Номер дома', **NULLABLE)
    provider = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE,
                                 verbose_name='Поставщик')
    products = models.ManyToManyField(Product, default=None, verbose_name='Продукты')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    debt = models.FloatField(default=0.00, verbose_name='задолженность перед поставщиком', null=True, blank=True)
