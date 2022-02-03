from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import stdForm
from .models import std ,myuser
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as authlogin
# Create your views here.




def loginusertoadmin(request):
    context={}
    if(request.method=='GET'):
        return render(request, 'loginusertoadmin.html')
    else:
        username = request.POST['name']
        password = request.POST['password']
        #check cred in User
        authuser= authenticate(username=username,password=password)
        #check cred in myuser
        user=myuser.objects.filter(username=username,password=password)

        if(authuser is not None and user is not  None):
            request.session['username']=username
            authlogin(request,authuser)
            return render(request,'base.html',context)
        else:
            context['errormsg'] = 'invlaid cred.'
            return render(request, 'loginusertoadmin.html', context)


def mylogout(request):
    request.session['username']=None
    return redirect('/employee/loginusertoadmin')           









def addusertoadmin(req):
    #add in user model
    #add in user auth
    context={}
   # context['adminuser']=User.objects.all()
    #context['users']=myuser.objects.all()
    if(req.method=='GET'):

       return render(req,'addusertoadmin.html',context)
    else:
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        myuser.objects.create(username=username,password=password)
        User.objects.create_user(username=username,email=email,password=password)
        return redirect('/admin')   







def registeruser(req):
    print(req.method)
    context={}
    if(req.method=='GET'):
        return render(req,'employee_register/register.html')
    else:
        myuser.objects.create(username=req.POST['username'], password=req.POST['password'])
        context['users']=myuser.objects.all()
        return HttpResponseRedirect('/employee/login')
def login(req):
    context={}
    if(req.method=='GET'):
        
       return render (req,'employee_register/login.html') 
    else:
        username=req.POST['username']
        password=req.POST['password']
        user=myuser.objects.filter(username=username,password=password)

        if(len(user)>0):
            user=user[0]   
        if(user):
            return redirect('/employee/list')
        else:
            context['errormsg']='invalid login'
            return render (req,'employee_register/login.html',context)   
def employee_list(request):
    context = {'employee_list': std.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = stdForm()
        else:
            employee = std.objects.get(pk=id)
            form = stdForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = stdForm(request.POST)
        else:
            employee = std.objects.get(pk=id)
            form = stdForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = std.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
