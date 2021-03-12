from django.shortcuts import render,redirect
from django.http import JsonResponse, response
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout



# Create your views here.

def veIndex(request):
    if request.user.is_authenticated and request.user.is_staff == True:
        return render(request, 'vendor/ve-index.html')
    else:
        return redirect('ve-login')

def veSignup(request):
    if request.method =='POST':
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
            user =  User.objects.create_user(username = username, email = email, password = password, is_staff = True)
            print('Vendor is created')
            return JsonResponse('true', safe=False)
    return render(request, 'vendor/ve-signup.html')

def veLogin(request):
    if request.user.is_authenticated and request.user.is_staff == True:
        return redirect('ve-index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                print('goto vendor home')
                auth.login(request, user)
                return JsonResponse('true', safe=False)
            else:
                print("incorrect username or password")
                return JsonResponse('false', safe=False)
        return render(request, 'vendor/ve-login.html')
    return render(request, 'vendor/ve-login.html')

def veLogout(request):
    logout(request)
    return redirect('ve-login')

def manage_product(request):
    if request.user.is_authenticated and request.user.is_staff == True:
        return render(request, 'vendor/manage-product.html')
    else:
        return redirect('ve-login')



def create_product(request):
    if request.user.is_authenticated and request.user.is_staff == True:
        
        return render(request, 'vendor/add-product.html')

    else:
        return redirect('ve-login')

