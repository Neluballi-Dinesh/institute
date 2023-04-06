from django.shortcuts import render,redirect,HttpResponse
from .models import Courses
from .models import contact,feedbackData
from .forms import RegisterationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import datetime as dt
date1=dt.datetime.now()

@login_required(login_url='login')
def homepage(request):
    return render(request,'homepage.html')


@login_required(login_url='login')
def contactpage(request):
    if request.method=="GET":
        return render(request,'contactpage.html')
    else:
        contact(
        name=request.POST['name'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        course=request.POST['course'],
        location=request.POST['location'],
        ).save()
        return redirect('contact')

@login_required(login_url='login')
def servicepage(request):
    courses=Courses.objects.all()
    return render(request,'servicepage.html',{'courses':courses})


@login_required(login_url='login')
def feedbackpage(request):
    if request.method=='GET':
        feedbacks=feedbackData.objects.all().order_by("-id")
        return render(request,'feedbackpage.html',{'feedbacks':feedbacks})
    else:
        feedbackData(
        content=request.POST['feedback'],
        date=date1
        ).save()
        feedbacks=feedbackData.objects.all().order_by("-id")
        return render(request,'feedbackpage.html',{'feedbacks':feedbacks})

@login_required(login_url='login')
def gallerypage(request):
    return render(request,'gallerypage.html')

def loginpage(request):
    if request.method=='GET':
        return render(request,'loginpage.html')

    else:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('invalid Username or password')


def logoutpage(request):
    logout(request)
    return redirect('login')


def registerpage(request):
    if request.method=='GET':
        form = RegisterationForm()
        return render(request,'registerpage.html',{'form':form})

    else:
        form=RegisterationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user=user.set_password(user.password)
            form.save()
            return redirect('login')
        else:
            return HttpResponse('Invalid form')
