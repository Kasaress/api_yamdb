import jwt
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

ROLE_CHOICES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **other_fields):
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

    def create_superuser(self, email, username, password, **other_fields):
        if not email:
            raise ValueError('Укажите адрес электронной почты')
        if not username:
            raise ValueError('Придумайте username')
        user = self.model(email=email, username=username,
                          is_staff=True, is_superuser=True, **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractUser):
    username = models.CharField(
        'Username',
        unique=True,
        blank=False,
        max_length=150,
    )
    email = models.EmailField(
        'E-mail address',
        unique=True,
        blank=False,
    )
    first_name = models.CharField(
        'first name',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        'last name',
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        'Биография пользователя?',
        blank=True
    )
    role = models.CharField(
        max_length=9,
        choices=ROLE_CHOICES,
        default='user'
    )
    confirmation_code = models.CharField(
        max_length=5, null=True,
        verbose_name='Код подтверждения'
    )
    # USERNAME_FIELD = 'email'  # Поле для входа в систему
    # REQUIRED_FIELDS = ['username', 'email']
    objects = CustomUserManager()

    # def __str__(self):
    #     """ Строковое представление модели (отображается в консоли) """
    #     return self.email

