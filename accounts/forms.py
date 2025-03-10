from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'phone_number')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username = username.lower()
        if len(username) < 5:
            raise ValidationError("Login must be at least 5 characters long")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        return email



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'telegram')




