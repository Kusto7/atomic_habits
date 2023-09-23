from django.db import models
from django.utils import timezone
from django_celery_beat.models import PeriodicTask

from users.models import User, NULLABLE


class Habit(models.Model):

    """Модель привычки"""

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Владелец привычки", **NULLABLE,
                              help_text="создатель привычки.")

    place = models.CharField(max_length=150, verbose_name="Место",
                             help_text="Место, в котором необходимо выполнять привычку.")

    time = models.TimeField(default=timezone.now, verbose_name="Время",
                            help_text="Время, когда необходимо выполнять привычку.")

    action = models.CharField(max_length=150, null=False, blank=False,
                              verbose_name="Действие", help_text="Действие, которое представляет из себя привычка.")

    is_pleasant = models.BooleanField(default=False, verbose_name="Признак приятной привычки",
                                      help_text="Привычка, которую можно привязать к выполнению полезной привычки")

    link_pleasant = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE,
                                      help_text="Привычка, которая связана с другой привычкой, "
                                                "важно указывать для полезных привычек, но не для приятных.")

    reward = models.CharField(max_length=150, verbose_name="Вознаграждение ", **NULLABLE,
                              help_text="Чем пользователь должен себя вознаградить после выполнения.")

    frequency = models.PositiveIntegerField(default=1, verbose_name='Периодичность',
                                            help_text="Периодичность выполнения привычки для напоминания в днях "
                                                      "(по умолчанию ежедневная)")

    duration = models.PositiveIntegerField(default=120, verbose_name='Время на выполнение',
                                           help_text="Время, которое предположительно потратит "
                                                     "пользователь на выполнение привычки.")

    is_public = models.BooleanField(default=False, verbose_name='Признак публичности',
                                    help_text="Привычки можно публиковать в общий доступ, "
                                              "чтобы другие пользователи могли брать в пример чужие привычки.")

    task = models.ForeignKey(PeriodicTask, on_delete=models.SET_NULL, verbose_name='Ссылка на периодическую задачу',
                             **NULLABLE)

    def __str__(self):
        loop_self = self
        message = f"я буду {self.action} в {self.time} в {self.place}\nВремя на выполнение: {self.duration}\n"
        while True:
            if loop_self.reward:
                return message + f"Вознаграждение: {loop_self.reward}"
            elif loop_self.link_pleasant is None:
                return message
            else:
                loop_self = loop_self.link_pleasant
                continue

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = 'Привычки'
