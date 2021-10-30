from django.db.models.signals import post_save
from django.dispatch import receiver

from box.models import Giveaway
from box.service import query_qualifying_users, generate_single_boxes


@receiver(post_save, sender="box.Giveaway")
def post_giveaway_create_actions(sender, instance, created, **kwargs):
    if not created:
        return
    users = query_qualifying_users(instance.provider.location)

    generate_single_boxes(instance.provider, instance)
    for user in users:
        print("initiating post_giveaway_actions")
        print(user.first_name)
