from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=5)
    email = models.EmailField()

    def __str__(self):
        return "%s"%(self.user)

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        print('create_customer_profile: a profile has been created')