import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import CIEmailField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from .managers import CustomUserManager
from .validators import validate_accepted


class CustomUser(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = CIEmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=250)
    phone_number = PhoneNumberField(blank=True)
    phone_number_confirmed = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    country = CountryField()
    accepted_terms_of_service = models.BooleanField(
        validators=[validate_accepted])
    accepted_privacy_policy = models.BooleanField(
        validators=[validate_accepted])
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
        'accepted_terms_of_service',
        'accepted_privacy_policy',
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
