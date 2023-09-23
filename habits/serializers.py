from rest_framework import serializers

from habits.models import Habit
from habits.validators import DurationValidator, FrequencyValidator, IsPleasantValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для привычки"""
    validators = [
        DurationValidator(field='duration'),
        FrequencyValidator(field='frequency'),
        IsPleasantValidator(field1='is_pleasant', field2='link_pleasant', field3='reward')
    ]

    class Meta:
        model = Habit
        fields = ['pk', 'place', 'time', 'action', 'is_pleasant', 'link_pleasant', 'reward', 'frequency', 'duration',
                  'is_public']
        