from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from accounts.forms import AccountChangePassword
from accounts.models import Account, Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Account)
class AccountAdmin(UserAdmin):
    model = Account
    form = UserChangeForm
    change_password_form = AccountChangePassword

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'date_joined',)
    list_display_links = list_display[:4]
    readonly_fields = ('last_login', 'date_joined',)
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    add_fieldsets = (
        *UserAdmin.add_fieldsets, (
            'Пользовательские поля', {
                'fields': (
                    'reset_password_key',
                    'email',
                )
            }
        )
    )
    fieldsets = (
        *UserAdmin.fieldsets, (
            'Пользовательские поля', {
                'fields': (
                    'reset_password_key',

                )
            }
        )
    )
