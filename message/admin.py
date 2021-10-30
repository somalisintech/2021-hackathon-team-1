from django.contrib import admin

# Register your models here.

from message.models import Messages
admin.site.register(Messages)