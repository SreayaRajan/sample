from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Register
from django.contrib import messages
from django.urls import reverse
# Create your views here.
def signin(request):
      if request.method=="POST":
         username=request.POST["uname"]
         password=request.POST["password"]
         user=Register.objects.get(username=username,password=password)
         if user is None:
             messages.error(request,'Invalid Password')
             return redirect ('signin')
         else:
             request.session['username']=username
             return redirect('home')
      return render(request,"login.html")
def register(request):
     if request.method=="POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        myreg=Register(name=name,phone=phone,email=email,username=username,password=password)
        myreg.save()
        return redirect('signin')
     return render(request,"register.html")

def index6(request):
    if'username' not in request.session: 
        return redirect('signin')
    return render(request,"indexnew.html")
def logout(request):
    if 'username' in request.session:
        #request.session.flush()
        return redirect('signin')
    return render(request,'login.html')
def viewall(request):
    if 'username' not in request.session:
        return redirect('signin')
    reg=Register.objects.all()
    context={
        'reg':reg,
    }
    return render(request,"viewreg.html",context)
def updatereg(request,pk):
    reg=Register.objects.get(id=pk)
    dic={
        'reg':reg
    }    
    return render(request,"register.html",dic)
def updatedata(request,pk):
    name=request.POST["name"]
    phone =request.POST["phone"]
    email=request.POST["email"]
    username=request.POST["username"]
    password=request.POST["passwordp"]
    reg = Register.objects.get(id=pk)
    reg.name = name
    reg.name = phone
    reg.name = email
    reg.name = username
    reg.name = password
    reg.save()
    return HttpResponseRedirect(reverse('viewall'))
