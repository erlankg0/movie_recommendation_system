from django.db import models
from django.contrib.auth.models import AbstractUser


class Gender(models.Model):
    CHOICES = (
        ('м', 'мужской'),
        ('ж', 'женский'),
    )
    name = models.CharField(
        max_length=1,
        choices=CHOICES,
        verbose_name='Пол',
        help_text='Пол пользователя',
        unique=True
    )

    def __str__(self):
        if self.name == 'м':
            return 'мужской'
        else:
            return 'женский'

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'
        db_table = 'gender'


class CustomUser(AbstractUser):
    first_name = models.CharField(
        max_length=30,
        verbose_name='Имя',
        help_text='Имя пользователя',
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name='Фамилия',
        help_text='Фамилия пользователя'
    )
    gender = models.ForeignKey(
        Gender,
        on_delete=models.PROTECT,
        verbose_name='Пол',
        help_text='Пол пользователя',
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='Email',
        help_text='Email пользователя',
        unique=True
    )
    secret = models.CharField(
        max_length=100,
        verbose_name='Секретный код',
        help_text='Секретный код пользователя для восстановления пароля',
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'user'
