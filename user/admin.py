from django.contrib import admin
from user.models import ServiceUser, Provider, TextMessage

admin.site.register(Provider)
admin.site.register(ServiceUser)
admin.site.register(TextMessage)
