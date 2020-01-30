from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'email',
            'full_name',
            'country',
            'phone_number',
            'date_of_birth',
            'accepted_terms_of_service',
            'accepted_privacy_policy',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'full_name',
            'country',
            'phone_number',
            'date_of_birth',
        )
