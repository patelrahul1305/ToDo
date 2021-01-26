from todo_list.models import ToDo
from rest_framework import serializers
from django.contrib.auth.models import User


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['task', 'description', 'done', 'user']
