from django.urls import path
from . import views
from .views import ToDoListView, ToDoDetailView, ToDoCreateView, ToDoUpdateView, ToDoDeleteView


urlpatterns = [
    path('', ToDoListView.as_view(), name='todo_home'),
    path('todo/<int:pk>/',  ToDoDetailView.as_view(), name='detail_todo'),
    path('todo/new/',  ToDoCreateView.as_view(), name='new_todo'),
    path('todo/update/<int:pk>/',  ToDoUpdateView.as_view(), name='update_todo'),
    path('todo/delete/<int:pk>/',  ToDoDeleteView.as_view(), name='delete_todo'),
]
