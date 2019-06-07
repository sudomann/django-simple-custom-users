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
            'accepted_TOS',
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