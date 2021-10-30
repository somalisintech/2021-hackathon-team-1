from django.contrib import admin
from user.models import ServiceUser, Provider

admin.site.register(Provider)
admin.site.register(ServiceUser)
