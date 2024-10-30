from django.contrib import admin
from .models import Buyer, Game

# Register your models here.


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # Поля для отображения в списке
    list_display = ('name', 'balance', 'age')
    # Поле для поиска по имени
    search_fields = ('name',)
    # Фильтр по возрасту
    list_filter = ('age',)

    # Поля, по которым можно кликнуть, чтобы перейти к редактированию записи.
    list_display_links = ('name',)
    # Делает поле редактируемым прямо из списка.
    list_editable = ('age',)
    # Сортировка объектов по умолчанию.
    ordering = ('name',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Поля для отображения
    list_display = ('title', 'cost', 'size', 'age_limited')
    # Поля для поиска по названию и описанию
    search_fields = ('title', 'description')
    # Фильтр по возрастному ограничению
    list_filter = ('age_limited',)
