from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todo/', views.ToDoList.as_view(), name="list_todo"),
    path('new_todo/', views.NewTodo.as_view(), name='new_todo'),
    path('<int:pk>/', views.ToDoDetail.as_view(), name='detail_todo'),
    path('<int:pk>/delete/', views.DeleteToDo.as_view(), name='delete_todo'),
    path('<int:pk>/edit/', views.UpdateToDo.as_view(), name='update_todo'),
    # Auth
    # admin: Denis, password: qwe
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('logined/', views.LoginUser.as_view(), name='logined'),
    path('logout/', LogoutView.as_view(), name='logout')
]
