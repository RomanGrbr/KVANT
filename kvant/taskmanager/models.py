from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    int_list_validator)
from django.db import models

STATUS_CHOICES = (
    ('created', 'Создан'),
    ('run', 'Запущен'),
    ('stopped', 'Остновлен')
)


class Task(models.Model):
    priority = models.IntegerField(verbose_name='Приоритет',
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
    status = models.CharField(verbose_name='Статус', max_length=20,
                              choices=STATUS_CHOICES, default='created')
    creation_time = models.TimeField(verbose_name='Время создания',
                                     auto_now_add=True)
    list_of_performers = models.CharField(verbose_name='Список исполнителей',
                                          max_length=20,
                                          validators=[int_list_validator])

    class Meta:
        ordering = ['-priority', 'creation_time']
