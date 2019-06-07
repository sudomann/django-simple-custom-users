from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_accepted(response):

    if response is False:
        raise ValidationError(
            _("You must agree in order to proceed")
        )
    else:
        return response