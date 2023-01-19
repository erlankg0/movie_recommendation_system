from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models


# Менеджер аккаунтов
class CustomUserManager(BaseUserManager):
    """
    Creates and saves a User with the given email, date of
    birth and password.
    """

    # создание пользователя
    def create_user(self, username, email, reset_password_key, password=None) -> None:
        if not email:
            raise ValueError("У пользователя должная быть email")
        if not username:
            raise ValueError("У пользователя должная быть username")
        if not reset_password_key:
            raise ValueError("У пользователя должен быть секретный ключ")

        user = self.model(
            email=self.normalize_email(email),  # нормализация email
            username=username,
            reset_password_key=reset_password_key
        )
        user.set_password(password)  # сохранения пароля
        user.save(using=self._db)  # сохранения пользователя
        return user

    def create_superuser(self, username, email, reset_password_key, password):
        user = self.create_user(
            email=email,
            username=username,
            reset_password_key=reset_password_key,
            password=password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Gender(models.Model):
    CHOICES = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )
    name = models.CharField(max_length=10, choices=CHOICES, default='Мужской', unique=True, verbose_name='Пол')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"


class Account(AbstractUser):
    # only add email field for login

    email = models.EmailField(
        verbose_name='Email',
        max_length=50,
        unique=True
    )  # email
    # секретный ключ для восстановления пароля
    reset_password_key = models.CharField(
        verbose_name='Секретный ключ для восстановления пароля',
        max_length=100,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)  # активный пользователь
    is_admin = models.BooleanField(default=False)  # администратор

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # логин по email
    REQUIRED_FIELDS = ['username', 'reset_password_key']  # Email & Password are required by default.

    def __str__(self):
        return self.email  # возвращает email
