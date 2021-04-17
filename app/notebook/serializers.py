from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import BooleanField

from rest_framework.serializers import Serializer, ListField, ChoiceField

from .models import Notebook


class UserSerializer(serializers.ModelSerializer):
    """ Автор заметки """

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined')

    def to_representation(self, instance):
        """ Переопределение вывода. Меняем формат даты в ответе """
        ret = super().to_representation(instance)
        # Конвертируем строку в дату по формату
        date_joined = datetime.strptime(ret['date_joined'], '%Y-%m-%dT%H:%M:%S.%f')
        # Конвертируем дату в строку в новом формате
        ret['date_joined'] = date_joined.strftime('%d %B %Y %H:%M:%S')
        return ret


class NotebookListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Notebook
        fields = "__all__"

    def to_representation(self, instance):
        """ Переопределение вывода. Меняем формат даты в ответе """
        ret = super().to_representation(instance)
        # Конвертируем строку в дату по формату
        date_add = datetime.strptime(ret['date_add'], '%Y-%m-%dT%H:%M:%S.%f')
        # Конвертируем дату в строку в новом формате
        ret['date_add'] = date_add.strftime('%d %B %Y %H:%M:%S')
        return ret


class FilterSerializer(Serializer):
    activity = ListField(child=ChoiceField(choices=Notebook.ACTIVITY_STATUS), required=False)
    important = BooleanField(required=False)
    public = BooleanField(required=False)


class NoteIdSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Notebook
        exclude = ('public',)
        read_only_fields = ['date_add', 'user', ]

    def to_representation(self, instance):
        """ Переопределение вывода. Меняем формат даты в ответе """
        ret = super().to_representation(instance)
        # Конвертируем строку в дату по формату
        date_add = datetime.strptime(ret['date_add'], '%Y-%m-%dT%H:%M:%S.%f')
        # Конвертируем дату в строку в новом формате
        ret['date_add'] = date_add.strftime('%d %B %Y %H:%M:%S')
        return ret
