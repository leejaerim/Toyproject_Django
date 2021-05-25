from django.db import models

# Create your models here.
#django automatically gives each model the id field with primary key
class Todo(models.Model):
    text = models.CharField(max_length=200)#Not Null
    isCompleted = models.SmallIntegerField(null=True)
    def __str__(self):
        return self.todo_text
    class Meta:
        db_table='todo'

class User(models.Model):
    user_name = models.CharField(max_length=16,default="Guest")
    #api_key = models.CharField(max_length=40, null=True)
    #reg_date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.user_name+str(self.id)
    class Meta:
        db_table='user'
class Room(models.Model):
    room_title = models.CharField(max_length=30)
    room_password = models.CharField(max_length=4,null=True)
    user_one = models.ForeignKey(User, on_delete=models.CASCADE)
    isAvailable = models.SmallIntegerField()
    def __str__(self):
        return self.room_title
    class Meta:
        db_table='room'

from django.contrib import admin

admin.site.register(Room) 