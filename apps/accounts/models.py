from django.contrib.auth.models import AbstractUser
from django.db import models


SEX = (
    ('MAN', 'Мужской'),
    ('WOMAN', 'Женский'),
)


class User(AbstractUser):
    """
    Создаем новую модель пользователя на основе стандартной
    и дополняем её своими полями
    """
    email = models.EmailField(
        max_length=30,
        unique=True
    )
    sex = models.CharField(
        verbose_name='Пол',
        choices=SEX,
        max_length=7
    )
    date_of_birth = models.DateField(
        verbose_name='День рождения',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='Активен',
        default=True,
    )

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Список пользователей"
        ordering = ('email',)
