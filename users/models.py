import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.postgres.fields import CIEmailField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class BaseAgreement(models.Model):
    # revision date should be the document version identifier
    effective_date = models.DateField(unique_for_date=True)

    is_current = models.BooleanField()

    date_created = models.DateTimeField(auto_now_add=True)

    # A new record with `is_curent` flag set to `True`
    # sets the existing `is_current` record (if any) to False
    def save(self, *args, **kwargs):
        if self.is_current:
            try:
                temp = self.__class__.objects.get(is_current=True)
                if self != temp:
                    temp.is_current = False
                    temp.save()
            except self.__class__.DoesNotExist:
                pass
        super(BaseAgreement, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class TermsOfService(BaseAgreement):
    pass


class PrivacyPolicy(BaseAgreement):
    pass


class SecurityPolicy(BaseAgreement):
    pass


class CustomUser(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    # this email field type is why this user model is
    # only compatible with Postgres
    email = CIEmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_modified = models.DateField(auto_now=True)
    terms_of_service_version = models.ForeignKey(
        TermsOfService, on_delete=models.PROTECT, null=True)
    security_policy_version = models.ForeignKey(
        SecurityPolicy, on_delete=models.PROTECT, null=True)
    privacy_policy_version = models.ForeignKey(
        PrivacyPolicy, on_delete=models.PROTECT, null=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
