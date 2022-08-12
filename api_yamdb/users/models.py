from typing import Any, Dict, Optional

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

ROLE_CHOICES = (
    (USER, USER),
    (MODERATOR, MODERATOR),
    (ADMIN, ADMIN),
)


class CustomUserManager(BaseUserManager):  # type: ignore
    """Кастомный менеджер модели User."""
    def create_user(
            self,
            username: str,
            email: str,
            password: Optional[str] = None,
            **other_fields: Dict[str, Any]) -> Any:
        if not email:
            raise ValueError('Укажите адрес электронной почты')
        if not username:
            raise ValueError('Придумайте username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
            username: str,
            email: str,
            password: Optional[str] = None,
            **other_fields: Dict[str, Any]) -> Any:
        if not email:
            raise ValueError('Укажите адрес электронной почты')
        if not username:
            raise ValueError('Придумайте username')
        user = self.model(email=email, username=username,
                          is_staff=True, is_superuser=True, **other_fields)
        user.set_password(password)
        user.save()
        return user


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
        'Биография пользователя?',
        blank=True
    )
    role: str = models.CharField(
        max_length=9,
        choices=ROLE_CHOICES,
        default='user'
    )
    confirmation_code: int = models.CharField(
        max_length=5, null=True,
        verbose_name='Код подтверждения'
    )
    objects = CustomUserManager()

    class Meta:
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_name'
            ),
        ]

    @property
    def is_moderator(self) -> bool:
        return bool(self.role == USER)

    @property
    def is_admin(self) -> bool:
        return bool(
            self.role == ADMIN
        )

    def __str__(self) -> str:
        """ Строковое представление модели (отображается в консоли) """
        return self.username
