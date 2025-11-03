"""Сериализаторы для модели задачи Task."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для модели задачи Task."""

    class Meta:
        """Метаданные сериализатора."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
