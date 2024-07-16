from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Link, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'create_data')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('type_level', 'email', 'country', 'city', 'street', 'house_number', 'provider_link', 'created_at',
                    'debt')
    list_filter = ('city',)
    actions = ['clear_debt']

    def provider_link(self, obj):
        if obj.provider:
            url = reverse('admin:app_link_change', args=[obj.provider.id])
            return format_html('<a href="{}">{}</a>', url, obj.provider.email)
        return "-"

    provider_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)
        self.message_user(request, "Задолженность перед поставщиком успешно очищена у выбранных объектов.")

    clear_debt.short_description = 'Очистить задолженность перед поставщиком'
