from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import ToDo
from .forms import NewToDoForm, RegisterForm, LoginForm


def index(request):
    return render(request, 'my_todo/startpage.html')


class ToDoList(ListView):
    paginate_by = 5
    model = ToDo
    template_name = 'my_todo/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return ToDo.objects.filter(author=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = NewToDoForm()
        return context


class ToDoDetail(LoginRequiredMixin, DetailView):
    model = ToDo
    context_object_name = 'todo'
    template_name = 'my_todo/detail_todo.html'


class NewTodo(LoginRequiredMixin, CreateView):
    form_class = NewToDoForm
    template_name = 'my_todo/new_todo.html'

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.author = self.request.user
        todo.save()
        return redirect('detail_todo', todo.pk)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['new'] = True
        return context


class DeleteToDo(LoginRequiredMixin, DeleteView):
    model = ToDo
    template_name = 'my_todo/detail_todo.html'
    success_url = reverse_lazy('list_todo')


class UpdateToDo(LoginRequiredMixin, UpdateView):
    model = ToDo
    form_class = NewToDoForm
    template_name = 'my_todo/detail_todo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['edit'] = True
        return context


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'my_todo/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("index")


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'my_todo/logined.html'
