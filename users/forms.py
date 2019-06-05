from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'email',
            'full_name',
            'phone_number',
            'date_of_birth',
            'agree_TOS_and_privacy',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'full_name',
            'phone_number',
            'date_of_birth',
        )