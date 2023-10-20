# Generated by Django 4.2.5 on 2023-09-23 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('habits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_celery_beat', '0018_improve_crontab_helptext'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='owner',
            field=models.ForeignKey(blank=True, help_text='создатель привычки.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец привычки'),
        ),
        migrations.AddField(
            model_name='habit',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_celery_beat.periodictask', verbose_name='Ссылка на периодическую задачу'),
        ),
    ]