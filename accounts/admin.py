from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'telegram', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'telegram',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('phone_number', 'telegram',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin,)
