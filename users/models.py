import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=250)
    phone_number = PhoneNumberField(blank=True)
    date_of_birth = models.DateField()
    country = CountryField()
    agree_TOS_and_privacy = models.BooleanField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_modified = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'full_name',
        'country',
        'phone_number',
        'date_of_birth',
        'agree_TOS_and_privacy',
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
