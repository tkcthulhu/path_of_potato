from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomMenuItem(ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):

        form = super().get_form(request, obj, **kwargs)
        is_manager = list(request.user.groups.filter(name='Manager'))

        if is_manager :
            form.base_fields['title'].disabled = True
            form.base_fields['description'].disabled = True
            form.base_fields['price'].disabled = True
            form.base_fields['spicy_level'].disabled = True
            form.base_fields['category'].disabled = True
            form.base_fields['cuisine'].disabled = True

        return form

admin.site.register( MenuItem, CustomMenuItem)