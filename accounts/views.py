from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms
from . import models


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    models = models.CustomUser
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    list_display = ('email', 'username', )