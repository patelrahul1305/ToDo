from django.shortcuts import render
#from django.contrib.auth.models import User
from rest_framework import viewsets
#from rest_framework import permissions, generics
from .serializers import ToDoSerializer
from todo_list.models import ToDo

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# class ToDoList(generics.ListAPIView):
#     serializer_class = ToDoSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return ToDo.objects.filter(user=user)
