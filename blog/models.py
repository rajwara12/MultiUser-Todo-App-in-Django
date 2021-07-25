from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    todo = models.TextField()
    timestamp = models.DateTimeField(blank=True,default=now)


    def __str__(self)  :
        return self.todo[0:13] + ' by ' + self.user.username




class Blog(models.Model):
    img= models.ImageField(upload_to="images")
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    desc = models.TextField()
    timestamp = models.DateTimeField(null=True)
    slug = models.CharField(max_length=30) 
    views = models.IntegerField(default=0)

    def __str__(self)  :
        return self.title[0:13] + ' by ' + self.author
       