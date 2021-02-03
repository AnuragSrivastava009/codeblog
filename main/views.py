from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import login,register,contact,item,Tutorial
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django import forms

from django.core.exceptions import ValidationError

      
from django.contrib import auth

# Create your views here.
def base(request):
    return render(request,'base.html')

def post(request):
    return render(request,'post.html')
def index(request):
    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    items = item.objects.all()
    series_urls = {}
    for m in items.all():
        part_one = Tutorial.objects.filter(title__title = m.title).earliest("tutorial_published")  
        series_urls[m] = part_one.tutorial_slug  

    return render(request,'index.html',{'part_ones' : series_urls})


def my_slug(request, my_slug):
    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if my_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug = my_slug)
        tutorial_from_series = Tutorial.objects.filter(title__title =this_tutorial.title).order_by('tutorial_published')
        this_tutorial_idx = list(tutorial_from_series).index(this_tutorial)

    return render(
        request,
        'post.html',
        {
            'tutorial':this_tutorial,
            'sidebar':tutorial_from_series,
            'this_tutorial_idx':this_tutorial_idx
        })

#def logins(request):
 #   return render(request,'login.html')
def logins(request):
    if request.method == 'POST':
        form  =AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

       
            user=authenticate(username= username, password=password)
      
        
            if user is not None:
                login(request, user)
                messages.info(request, f"login  successfully! you are now logged as {username}")
                return redirect('/login.html')
            else:
                messages.error(request, 'invalid credential! please try again.')
            
        else:
            messages.error(request, 'invalid username or password.')   
    form = AuthenticationForm()
    return render(request=request,
                  template_name = "login.html",
                  context={"form":form} )

#def register(request):
 #   return render(request,'register.html')

def registers(request):
    if request.method =='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            username=form.cleaned_data.get('username')
        
            messages.success(request, f"register successfully! new user created:{username}")
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect("main:index")
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}: {form.error_messages[msg]}")
            return render(request=request,
                      template_name ="register.html",
                      context={"form":form} )
    form=UserCreationForm
    return render(
        request=request,
        template_name ="register.html",              
        context={"form":form} 
        )              

def about(request):
    return render(request,'about.html')
#def contact(request):
 #   return render(request,'contact.html')

def contacts(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        message=request.POST.get('message')
        Contact = contact(nam=name, email=email, message=message,phoneno=phoneno,)
        Contact.save()
        messages.success(request, 'message send successfully')
    return render(request,'contact.html')





 