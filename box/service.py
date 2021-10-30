from typing import Optional

from django.contrib.gis.geos import Point
from django.db.models import QuerySet

from django.db.models.signals import post_save
from django.dispatch import receiver

from box.models import Giveaway, Box
from user.models import ServiceUser
from django.contrib.gis.measure import Distance


def query_qualifying_users(provider_point: Point, radius: Optional[int] = 10) -> QuerySet:
    return ServiceUser.objects.filter(location__distance_lt=(provider_point, Distance(km=radius)))


def generate_single_boxes(provider, giveaway):
    for box in range(giveaway.units):
        Box.objects.create(giveaway=giveaway)



