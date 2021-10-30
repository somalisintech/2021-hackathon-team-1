from django.db import models

from user.models import ServiceUser
# Create your models here.

# TODO: write a database model that holds all the message that went sent to a user.

# what the message said. who the message was sent to and what time the message was sent.

class Messages(models.Model):
    content = models.CharField(max_length=160)
    sent_to = models.ForeignKey(ServiceUser, on_delete=models.DO_NOTHING)
    timestamp  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} was sent to {self.sent_to} at {self.timestamp}!"
 