from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from . import models


@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['number', 'point_value']
    order_by = ['number']


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'round_number', 'status', 'started_at']
    order_by = ['started_at']


@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'game', 'points']


@admin.register(models.Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['game']


@admin.register(models.PlayerCardCollection)
class PlayerCardCollectionAdmin(admin.ModelAdmin):
    list_display = ['player', 'collection']


@admin.register(models.TableCardCollection)
class TableCardCollectionAdmin(admin.ModelAdmin):
    list_display = ['table', 'collection']


@admin.register(models.CardCollection)
class CardCollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'cards_count']

    @admin.display(ordering='cards_count')
    def cards_count(self, cardcollection):
        url = (reverse('admin:cardgame_card_changelist')
               + '?'
               + urlencode({
                   'cardcollection__id': str(cardcollection.id)
               }))
        return format_html('<a href="{}">{}</a>', url, cardcollection.cards_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            cards_count=Count('cards')
        )
