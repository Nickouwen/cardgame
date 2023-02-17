from django.contrib import admin

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
    list_display = ['name']
