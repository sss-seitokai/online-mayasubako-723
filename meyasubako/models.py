from django.db import models
from django.contrib.auth.models import User

# user = User.objects.get(id=1)
# Create your models here.
class Opinion(models.Model):
  title = models.CharField(max_length=16) 
  content = models.CharField(max_length=10000)
  who = models.CharField(max_length=50)
  student_email = models.CharField(max_length=255,default='example@gmail.com')
  date_added = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(default=1)
  def __str__(self):
    return self.title

class TimeLine(models.Model):
  opinion = models.ForeignKey(Opinion,on_delete=models.CASCADE)
  title = models.CharField(max_length=10000)
  content = models.CharField(max_length=10000)
  date_added = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.title
  
