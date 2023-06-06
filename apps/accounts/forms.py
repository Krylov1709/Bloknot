from django_registration.forms import RegistrationForm
from apps.accounts.models import User


class MyRegistrationForm(RegistrationForm):
    '''
    Создаем регистрационной формы для работы с собственной моделью пользователя
    '''
    class Meta(RegistrationForm.Meta):
        model = User
        