from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, PrivacyPolicy, SecurityPolicy, TermsOfService


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('uuid', 'email', 'is_staff', 'is_active',
        'terms_of_service_version'), 'security_policy_version', 'privacy_policy_version')
    list_filter=('uuid', 'email', 'is_staff', 'is_active',
        'terms_of_service_version'), 'security_policy_version', 'privacy_policy_version')
    fieldsets=(
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets=(
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields=('uuid', 'email', 'full_name')
    ordering=('email',)


common_policy_fields=(
    'is_current', 'document_identifier', 'note', 'date_created')


class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display=common_policy_fields


class SecurityPolicyAdmin(admin.ModelAdmin):
    list_display=common_policy_fields


class TermsOfServiceAdmin(admin.ModelAdmin):
    list_display=common_policy_fields


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
admin.site.register(SecurityPolicy, SecurityPolicyAdmin)
admin.site.register(TermsOfService, TermsOfServiceAdmin)
