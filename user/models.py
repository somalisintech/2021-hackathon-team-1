from django.db import models


class ServiceUser(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Provider(models.Model):
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Message(models.Model):
    response = models.PositiveIntegerField()

    def __str__(self):
        return self.response


