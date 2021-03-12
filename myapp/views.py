from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.http import JsonResponse, response
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect("landing")
    else:
        return render(request, 'myapp/index.html')



def login(request):
    if request.user.is_authenticated:
        return redirect("landing")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                print('goto home')
                auth.login(request, user)
                return JsonResponse('true', safe=False)
            else:
                print("incorrect username or password")
                return JsonResponse('false', safe=False)
        return render(request, 'myapp/login.html')


def signup(request):
    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            print('username is alredy is taken')
            return JsonResponse('false1', safe=False)
        elif User.objects.filter(email=email).exists():
            print('email is already taken')
            return JsonResponse('false2', safe=False)
        else:
            user =  User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password)
            print('user is created')
            return JsonResponse('true', safe=False)
    return render(request, 'myapp/signup.html')


def landing(request):
    if request.user.is_authenticated:
        return render(request, 'myapp/landing.html')
    else:
        return redirect("login")

def userlogout(request):
    logout(request)
    return redirect('login')