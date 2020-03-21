from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CHOICES = [
        ('G', 'Guest'),
        ('E', 'Upwork'),
        ('F', 'Freelance'),
        ('C', 'Colleague')
    ]
    clienttype = models.CharField(verbose_name="Client Type", choices=CHOICES, max_length=20)
    country = CountryField()
    phoneno = PhoneNumberField()
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
        instance.profile.save()
