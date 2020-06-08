from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=10)
    number=models.CharField(max_length=15)
    sex=models.CharField(max_length=5)
    date=models.DateField(blank=True,null=True)
    def __str__(self):
        return u'名字 is %s 学号 is %s  性别 is %s'%(self.name,self.number,self.sex)
# Create your models here.
