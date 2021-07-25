 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Todo, Blog
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')

def todo(request):
    todo = request.POST.get('todo')
    user = request.user
    if request.method=='POST':
        
        todos = Todo(user=user,todo=todo)
        todos.save()
        messages.success(request,"Your Todo has been saved")
        return redirect('todo')

    else:
        mytodo = Todo.objects.filter(user=user)

        return render(request,'blog/todo.html',{'todos':mytodo})

def todo_del(request,todo_del):
    Todo.objects.get(id=todo_del).delete()
    messages.success(request,"Your Todo has sucessfully deleted")

    return redirect('todo')

def blog(request):
    allpost = Blog.objects.all()

    return render(request,'blog/blog.html',{'posts':allpost})        

def blogpost(request,slug):
    rpost = Blog.objects.filter(slug=slug).first() 
    rpost.views = rpost.views+1
    rpost.save()
    return render(request,'blog/blogpost.html',{'post':rpost})





def handlesignup(request):
    username= request.POST.get('username')
    email= request.POST.get('email')
    pass1= request.POST.get('pass1')
    pass2= request.POST.get('pass2')    
    if pass1 != pass2:
        messages.error(request,"Your Password Does'nt match")
        return redirect('index')
    myuser = User.objects.create_user(username,email,pass1)   
    myuser.save() 
    messages.success(request,"Your account has been created sucessfully")
    return redirect('index')


def handlelogin(request):
    username = request.POST.get('username')   
    pass1 = request.POST.get('pass1')
    user = authenticate(username=username,password=pass1)
    if user is not None:
        login(request,user)
        messages.success(request,"Your Login sucessfully")
        return redirect('index')
    else:
        messages.error(request,"Invalid Crediants")
        return redirect('index')
    


def handlelogout(request):
    logout(request)
    messages.success(request,"Your Logout sucessfully")
    return redirect('index')  
