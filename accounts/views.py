from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView



class BaseLogoutView(TemplateView):
    template_name = 'registration/logout.html'

class LoginView(AuthLoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        """ Login sahifasi uchun qo‘shimcha context qo‘shish """
        context = super().get_context_data(**kwargs)  # Standart contextni olish
        context["lang"] = settings.GLOBAL_LANG  # `.lang` fayldan tarjimalarni qo‘shish
        return context


class LangView():
    """Barcha `CreateView` lar uchun `.lang` ma’lumotini qo‘shuvchi sinf"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lang"] = settings.GLOBAL_LANG  # `.lang` fayldan ma’lumot olish
        return context

class RegistrationView(LangView, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class UserProfileView(LangView, DetailView):
    model = get_user_model()
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

class UserProfileUpdateView(LangView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'user_profile_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk or self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy('user_profile', args=[self.request.user.id])

class SupportView(LangView, TemplateView):
    template_name = 'support.html'




