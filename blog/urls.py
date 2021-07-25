 
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name="index"), 
    path('handlesignup',views.handlesignup,name="handlesignup"),
    path('handlelogin',views.handlelogin,name="handlelogin"),
    path('handlelogout',views.handlelogout,name="handlelogout"),
    path('todo/',views.todo,name="todo"),
    path('todo/todo_del/<int:todo_del>',views.todo_del,name="todo_del"),
    path('blog/',views.blog,name="blog"),
    path('blog/<str:slug>',views.blogpost,name="blogpost"),
]
