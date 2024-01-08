from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=50, null = True)
    designation = models.CharField(max_length=100,null = True)
    contact = models.CharField(max_length=10,null = True)
    gender = models.CharField(max_length=10, null = True)
    joiningdate = models.DateField(null = True)
    def __str__(self):
        return self.user.username
    
class EmployeeEducation(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        coursepg = models.CharField(max_length=100, null=True)
        Schoolclgpg = models.CharField(max_length=200, null = True)
        yearofpassingpg = models.CharField(max_length=20,null = True)
        percentagepg = models.CharField(max_length=30,null = True)
        
        coursegra = models.CharField(max_length=100, null=True)
        Schoolclggra = models.CharField(max_length=100, null = True)
        yearofpassinggra = models.CharField(max_length=20,null = True)
        percentagegra = models.CharField(max_length=30,null = True)
        
        coursessc = models.CharField(max_length=100, null=True)
        Schoolclgssc = models.CharField(max_length=100, null = True)
        yearofpassingssc = models.CharField(max_length=20,null = True)
        percentagessc = models.CharField(max_length=30,null = True)
        
        coursehsc = models.CharField(max_length=100, null=True)
        Schoolclghsc = models.CharField(max_length=100, null = True)
        yearofpassinghsc = models.CharField(max_length=20,null = True)
        percentagehsc = models.CharField(max_length=30,null = True)
        
def __str__(self):
        return self.user.username
    
class EmployeeExperience(models.Model):
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        company1name = models.CharField(max_length=100,null = True)
        company1design= models.CharField(max_length=100,null = True)
        company1salary = models.CharField(max_length=100,null = True)
        company1duration= models.CharField(max_length=100,null = True)
        
        company2name = models.CharField(max_length=100,null=True)
        company2design = models.CharField(max_length=100,null = True)
        company2salary = models.CharField(max_length=100,null = True)
        company2duration= models.CharField(max_length=100,null = True)
        
        company3name = models.CharField(max_length=100,null=True)
        company3design = models.CharField(max_length=100,null = True)
        company3salary = models.CharField(max_length=100,null = True)
        company3duration= models.CharField(max_length=100,null = True)
        
       
        
def __str__(self):
        return self.user.username
    
    
class CandidateDetails(models.Model):
        # user = models.ForeignKey(User,on_delete=models.CASCADE)
        Name = models.CharField(max_length=100, null=True)
        Email = models.CharField(max_length=200, null = True)
        Date_of_Birth = models.CharField(max_length=20,null = True)
        Contact = models.CharField(max_length=30,null = True)
        
        address = models.CharField(max_length=100, null=True)
        city = models.CharField(max_length=100, null = True)
        State = models.CharField(max_length=20,null = True)
        country = models.CharField(max_length=30,null = True)
        
        School = models.CharField(max_length=100, null=True)
        Marks10 = models.CharField(max_length=100, null = True)
        Marks12 = models.CharField(max_length=20,null = True)
        College = models.CharField(max_length=30,null = True)
        
        graduation_score = models.CharField(max_length=100, null=True)
        Backlogs = models.CharField(max_length=100, null = True)
        Resume = models.CharField(max_length=20,null = True)
       