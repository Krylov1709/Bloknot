from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from apps.accounts.forms import MyRegistrationForm

urlpatterns = [
    path('register/',
        RegistrationView.as_view(form_class=MyRegistrationForm),
        name='регистрация',
    ),
    path('', include('django_registration.backends.one_step.urls')),
    path('', include('django.contrib.auth.urls')),
]
