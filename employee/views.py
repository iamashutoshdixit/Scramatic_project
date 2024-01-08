from turtle import back
from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    
    if request.method == "POST":
       error= ""
       fn = request.POST['firstname']
       ln = request.POST['lastname']
       ec = request.POST ['employeecode']
       mail = request.POST['email']
       pwd = request.POST['pwd']
    try:
        user = User.objects.create_user(first_name = fn, last_name = ln, username=mail, password=pwd)
        EmployeeDetail.objects.create(user = user,empcode=ec)
        EmployeeExperience.objects.create(user = user)
        EmployeeEducation.objects.create(user = user)
        error = "no"
    except:
        error = "yes"
              
    return render(request,'registration.html',locals())
def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username= u, password= p)
        
        if user:
            login(request, user)
            
            error = "no"

        elif ((u=="hr@gmail.com") and (p=="hr")):
            return render(request,'hr_home.html',locals())

            error="hr"

        else:
            
            error ="yes"
        
    return render(request,'emp_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request,'emp_home.html')
def Logout(request):
    logout(request)
    return redirect('index')
    


def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error= ""
    user = request.user    
    employee = EmployeeDetail.objects.get(user=user)    
    if request.method == "POST":         
       fn = request.POST['firstname']
       ln = request.POST['lastname']
       ec = request.POST ['employeecode']
       dept = request.POST['department']
       designation = request.POST['designation']
       contact = request.POST['contact']
       jdate = request.POST['jdate']
       gender = request.POST['gender']
       
       employee.user.first_name=fn
       employee.user.last_name=ln
       employee.empcode=ec
       employee.empdept=dept
       employee.designation=designation
       employee.contact=contact
       employee.gender=gender
       
       if jdate:
           employee.joiningdate = jdate
       
    try:
        employee.save()
        employee.user.save()
      
        error = "no"
    except:
        error = "yes"
    return render(request,'profile.html',locals())
def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username= u, password= p)
        try:
            if user.is_staff:
                login(request, user)
            
                error = "no"
                            
        except:
            
            error ="yes"
        
    return render(request,'admin_login.html',locals())

def myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user    
    experience = EmployeeExperience.objects.get(user=user)    
    
    return render(request,'myexperience.html',locals())

def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error= ""
    user = request.user    
    experience = EmployeeExperience.objects.get(user=user)    
    if request.method == "POST":         
       company1name = request.POST['company1name']
       company1design = request.POST['company1design']
       company1salary = request.POST ['company1salary']
       company1duration = request.POST['company1duration']
       
       company2name = request.POST['company2name']
       company2design = request.POST['company2design']
       company2salary = request.POST ['company2salary']
       company2duration = request.POST['company2duration']
       
       company3name = request.POST['company3name']
       company3design = request.POST['company3design']
       company3salary = request.POST ['company3salary']
       company3duration = request.POST['company3duration']
       
       experience.company1name=company1name
       experience.company1design=company1design
       experience.company1salary=company1salary
       experience.company1duration=company1duration
       
       experience.company2name=company2name
       experience.company2esign=company2design
       experience.company2salary=company2salary
       experience.company2duration=company2duration
       
       experience.company3name=company3name
       experience.company3design=company3design
       experience.company3salary=company3salary
       experience.company3duration=company3duration
       
                   
       if experience:
           experience.save()          
            
           error = "no"
       else:
            
            error ="yes"
    return render(request,'edit_experience.html',locals())

def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user    
    education = EmployeeEducation.objects.get(user=user)    
    
    return render(request,'my_education.html',locals())

def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error= ""
    user = request.user    
    education= EmployeeEducation.objects.get(user=user)    
    if request.method == "POST":         
       pgcourse = request.POST['pgcourse']
       pgcollege = request.POST['pgcollege']
       pgyof = request.POST ['pgyof']
       pgper = request.POST['pgper']
       
       gracourse = request.POST['gracourse']
       gracollege = request.POST['gracollege']
       grayof = request.POST ['grayof']
       graper = request.POST['graper']
       
       ssccourse = request.POST['ssccourse']
       ssccollege = request.POST['ssccollege']
       sscyof = request.POST ['sscyof']
       sscper = request.POST['sscper']
       
       hsccourse = request.POST['hsccourse']
       hsccollege = request.POST['hsccollege']
       hscyof = request.POST ['hscyof']
       hscper = request.POST['hscper']
       
        
       
       education.coursepg=pgcourse
       education.Schoolclgpg= pgcollege
       education.yearofpassingpg=pgyof
       education.percentagepg= pgper
       
       education.coursegra =gracourse
       education.Schoolclggra= gracollege
       education.yearofpassinggra=grayof
       education.percentagegra= graper
       
       education.coursessc=ssccourse
       education.Schoolclgssc= ssccollege
       education.yearofpassingssc=sscyof
       education.percentagessc= sscper
       
       education.coursehsc=hsccourse        
       education.Schoolclghsc= hsccollege
       education.yearofpassinghsc=hscyof
       education.percentagehsc= hscper
       
       
                   
       if education:
           education.save()          
            
           error = "no"
       else:
            
            error ="yes"
    return render(request,'edit_myeducation.html',locals())

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error= ""
    user = request.user    
        
    if request.method == "POST":         
       c=request.POST['currentpassword']
       n=request.POST['newpassword']
       
       try:
           if user.check_password(c):
               user.set_password(n)
               user.save()
               error = "no"
           else:
               error ="not"
               
       except:
           error="yes"
              
           
       
    return render(request,'change_password.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def admin_changepassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error= ""
    user = request.user    
        
    if request.method == "POST":         
       c=request.POST['currentpassword']
       n=request.POST['newpassword']
       
       try:
           if user.check_password(c):
               user.set_password(n)
               user.save()
               error = "no"
           else:
               error ="not"
               
       except:
           error="yes"
              
           
       
    return render(request,'admin_changepassword.html',locals())

def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee=EmployeeDetail.objects.all()
    return render(request,'all_employee.html',locals())

def delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('all_employee')

def edit_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error= ""
       
    employee = EmployeeDetail.objects.get(id=pid)    
    if request.method == "POST":         
       fn = request.POST['firstname']
       ln = request.POST['lastname']
       ec = request.POST ['employeecode']
       dept = request.POST['department']
       designation = request.POST['designation']
       contact = request.POST['contact']
       jdate = request.POST['jdate']
       gender = request.POST['gender']
       
       employee.user.first_name=fn
       employee.user.last_name=ln
       employee.empcode=ec
       employee.empdept=dept
       employee.designation=designation
       employee.contact=contact
       employee.gender=gender
       
       if jdate:
           employee.joiningdate = jdate
           try:
               employee.save()
               employee.user.save()
      
               error = "no"
           except:
               error = "yes"
    return render(request,'edit_profile.html',locals())

def edit_education1(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error= ""
    user= User.objects.get(id=pid)  
    education= EmployeeEducation.objects.get(user=user)    
    if request.method == "POST":         
       pgcourse = request.POST['pgcourse']
       pgcollege = request.POST['pgcollege']
       pgyof = request.POST ['pgyof']
       pgper = request.POST['pgper']
       
       gracourse = request.POST['gracourse']
       gracollege = request.POST['gracollege']
       grayof = request.POST ['grayof']
       graper = request.POST['graper']
       
       ssccourse = request.POST['ssccourse']
       ssccollege = request.POST['ssccollege']
       sscyof = request.POST ['sscyof']
       sscper = request.POST['sscper']
       
       hsccourse = request.POST['hsccourse']
       hsccollege = request.POST['hsccollege']
       hscyof = request.POST ['hscyof']
       hscper = request.POST['hscper']
       
        
       
       education.coursepg=pgcourse
       education.Schoolclgpg= pgcollege
       education.yearofpassingpg=pgyof
       education.percentagepg= pgper
       
       education.coursegra =gracourse
       education.Schoolclggra= gracollege
       education.yearofpassinggra=grayof
       education.percentagegra= graper
       
       education.coursessc=ssccourse
       education.Schoolclgssc= ssccollege
       education.yearofpassingssc=sscyof
       education.percentagessc= sscper
       
       education.coursehsc=hsccourse        
       education.Schoolclghsc= hsccollege
       education.yearofpassinghsc=hscyof
       education.percentagehsc= hscper
       
       
                   
       if education:
           education.save()          
            
           error = "no"
       else:
            
            error ="yes"
    return render(request,'edit_education1.html',locals())

def edit_experience1(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error= ""
    user = User.objects.get(id=pid)   
    experience = EmployeeExperience.objects.get(user=user)    
    if request.method == "POST":         
       company1name = request.POST['company1name']
       company1design = request.POST['company1design']
       company1salary = request.POST ['company1salary']
       company1duration = request.POST['company1duration']
       
       company2name = request.POST['company2name']
       company2design = request.POST['company2design']
       company2salary = request.POST ['company2salary']
       company2duration = request.POST['company2duration']
       
       company3name = request.POST['company3name']
       company3design = request.POST['company3design']
       company3salary = request.POST ['company3salary']
       company3duration = request.POST['company3duration']
       
       experience.company1name=company1name
       experience.company1design=company1design
       experience.company1salary=company1salary
       experience.company1duration=company1duration
       
       experience.company2name=company2name
       experience.company2esign=company2design
       experience.company2salary=company2salary
       experience.company2duration=company2duration
       
       experience.company3name=company3name
       experience.company3design=company3design
       experience.company3salary=company3salary
       experience.company3duration=company3duration
       
                   
       if experience:
           experience.save()          
            
           error = "no"
       else:
            
            error ="yes"
    return render(request,'edit_experience1.html',locals())



def Aboutus(request):
    # if not request.user.is_authenticated:
    #     return redirect('emp_home')
    return render(request,'Aboutus.html')

def apply_job(request):
    if request.method == "POST":
       error= ""
       name = request.POST['name']
       email = request.POST['email']
       dob = request.POST ['dob']
       contactNo = request.POST['contactNo']
       Address = request.POST['Address']
       City = request.POST['City']
       state = request.POST['state']
       Country = request.POST['Country']
       School_Name = request.POST['School_Name']
       Marks10th = request.POST['Marks10th']
       Marks12th = request.POST['Marks12th']
       College_Name = request.POST['College_Name']
       graduation_marks = request.POST['graduation_marks']
       backlogs = request.POST['backlogs']
       resume= request.POST['myfile']
       
    try:
        user=User.objects.create_user(Name=name,Email=email,Date_of_Birth=dob,Contact=contactNo,address=Address,
                    city=City,State=state,country=Country,School=School_Name,Marks10=Marks10th,Marks12=Marks12th,
                    College=College_Name,graduation_score=graduation_marks,Backlogs=backlogs,Resume=resume)
        # CandidateDetails.objects.create(user=user)
        error = "no"
    except:
        error = "yes"
        print("exception")
    return render(request,'apply_job.html',locals())
   
def hr_home(request):
    # if not request.user.is_authenticated:
    #     return redirect('emp_login')
    return render(request,'hr_home.html')