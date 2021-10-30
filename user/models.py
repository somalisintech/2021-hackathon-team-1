from django.contrib.gis.db.models import PointField
from django.db import models


class AbstractUser(models.Model):
    phone_number = models.CharField(max_length=128)
    location = PointField(blank=True, null=True)

    def get_coordinates(self):
        return list(getattr(self.location, 'coords', [])[::-1])

    class Meta:
        abstract = True


class ServiceUser(AbstractUser):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Provider(AbstractUser):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
