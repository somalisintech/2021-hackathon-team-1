from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from user.models import ServiceUser, Provider

# admin.site.register(Provider)


@admin.register(Provider)
class ServiceUserAdmin(OSMGeoAdmin):
    list_display = ['id', 'name', 'location']
    default_lon = 5129656
    default_lat = 463746
    default_zoom = 7


@admin.register(ServiceUser)
class ServiceUserAdmin(OSMGeoAdmin):
    list_display = ['id', 'first_name', 'last_name', 'location']
    default_lon = 5129656
    default_lat = 463746
    default_zoom = 7
