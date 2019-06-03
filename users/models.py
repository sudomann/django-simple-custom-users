from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    full_name = models.CharField(max_length=200)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = PhoneNumberField(blank=True)
    date_of_birth = models.DateField()
    # country = 
    agree_tos_and_privacy = models.BooleanField(default=False)
    last_modified = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email