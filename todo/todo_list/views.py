from django.shortcuts import render
from .models import ToDo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import date


class ToDoListView(ListView):
    model = ToDo
    ordering = ['-created_at']


class ToDoDetailView(DetailView):
    model = ToDo


class ToDoCreateView(CreateView):
    model = ToDo
    fields = ['task', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ToDoUpdateView(UpdateView):
    model = ToDo
    fields = ['task', 'description', 'done']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.completed_at = date.today()
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        return self.request.user == todo.user

class ToDoDeleteView(DeleteView):
    model = ToDo
    success_url = '/'

    def test_func(self):
        todo = self.get_object()
        return self.request.user == todo.user
