
from email.policy import default

from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

ROLE_CHOICES = (
    (USER, 'Пользователь'),
    (MODERATOR, 'Модератор'),
    (ADMIN, 'Администратор'),
)


class CustomUser(AbstractUser):  # type: ignore
    """Кастомная модель User.
       Позволяет при создании запрашивать емейл и юзернейм.
    """
    username: str = models.CharField(
        'Username',
        unique=True,
        blank=False,
        max_length=150,
    )
    email: str = models.EmailField(
        'E-mail address',
        unique=True,
        blank=False,
    )
    first_name: str = models.CharField(
        'first name',
        max_length=150,
        blank=True
    )
    last_name: str = models.CharField(
        'last name',
        max_length=150,
        blank=True
    )
    bio: str = models.TextField(
        'Биография пользователя',
        blank=True
    )
    role: str = models.CharField(
        max_length=len(max(ROLE_CHOICES)),
        choices=ROLE_CHOICES,
        default='user'
    )
    confirmation_code: str = models.CharField(
        max_length=5, null=True,
        verbose_name='Код подтверждения',
        default=' '
    )

    class Meta:
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_name'
            ),
        ]

    def __str__(self) -> str:
        """Строковое представление модели (отображается в консоли)."""
        return self.username
