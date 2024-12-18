from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Please, use another name. This name is already being used')
            return redirect('signup')
        
        else:
            if password != password2:
                messages.info(request,'The password does not match!')
                return redirect('signup')
            
            else:
                User.objects.create_user(username=username,password=password)
                return redirect('login')


    else:
        return render(request,'signup.html')
    

def login(request):
    if request.method== "POST":
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Credentials are not valid!")
            return redirect('login')

    else:
        return render(request, 'login.html')
    


def logout(request):
    auth.logout(request)
    return redirect('/')