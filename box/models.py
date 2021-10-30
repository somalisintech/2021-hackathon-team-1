from django.db import models


from user.models import Provider, ServiceUser


class Giveaway(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    units = models.IntegerField(default=1)
    single_unit_weight = models.IntegerField(default=1)
    produce_name = models.CharField(max_length=128)
    description = models.TextField(max_length=5000)

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.units} boxes of {self.produce_name}"


class Box(models.Model):
    available = models.BooleanField(default=True)
    giveaway = models.ForeignKey(Giveaway, on_delete=models.CASCADE)

    given_to = models.ForeignKey(ServiceUser, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"{self.giveaway.produce_name}-{self.giveaway.single_unit_weight}"

    def save(self, *args, **kwargs):
        if self.given_to:
            self.available = False
        return super().save(*args, **kwargs)



""""

On giveaway creation -- create all the boxes
How does the farmer input the data to make a giveaway

farmer has excess produces. they input what they have. description, product name, how many units, weight per unit, when to pick up by

-------------------------
WHO DO WE EXTEND OFFER TO 

location -- query by location 

business logic --> priority 

boxes under subscribed -- do you make the location bigger // or a waiting list? 

who gets the message 

-------------------------
CONVERSATION WITH SERVICE USER 


reply with the response 

confirmation text

ability to cancel 


______________
 
"""