from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForms(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='Не обязательное поле Введите номер телефона')
    username = forms.CharField(max_length=150, required=True)
    usable_password = None

    class Meta():
        model = CustomUser
        fields = ('email', 'username','first_name', 'last_name', 'password1', 'password2')


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Телефон должен состоять из цифр')
        return phone_number