from django import forms
from .models import User
# from django.contrib.auth1.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': _("Логин"),
            'password1': _("Пароль"),
            'password2': _('Проверка пароля'),
        }
