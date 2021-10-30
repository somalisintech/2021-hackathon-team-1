from django.contrib import admin
from box.models import Box, Giveaway


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ['id', 'available', 'giveaway', 'given_to']


@admin.register(Giveaway)
class GiveawayAdmin(admin.ModelAdmin):
    pass
