from django.urls import path
from .views import RegistrationView, UserProfileView, UserProfileUpdateView, SupportView, LoginView, BaseLogoutView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('exit/', BaseLogoutView.as_view(), name='exit'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("login/", LoginView.as_view(), name="login"),
    path('support/', SupportView.as_view(), name='support'),
    path('users/profile_update/<int:pk>/', UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('users/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]