from django.contrib import admin
from account.models import CustomUser, Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
# Register your models here.
