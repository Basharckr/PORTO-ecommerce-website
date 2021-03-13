from django.shortcuts import render, redirect
from django.http import JsonResponse, response
from django.contrib.auth.models import User, auth
from .models import Products
# from django.core.files import File
from owner.models import Category
from django.contrib.auth import logout


# Create your views here.

def veIndex(request):
    if request.user.is_authenticated and request.user.is_staff == True:
        return render(request, 'vendor/ve-index.html')
    else:
        return redirect('ve-login')


def veSignup(request):
    if request.method == 'POST':
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
            user = User.objects.create_user(
                username=username, email=email, password=password, is_staff=True)
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


def add_product(request):
    if request.user.is_authenticated and request.user.is_staff == True:
        category = Category.objects.all()

        if request.method == 'POST':
            product_id = request.POST['product_id']
            product_name = request.POST['product_name']
            product_categorie = request.POST['product_categorie']
            print(product_categorie)
            product_price = request.POST['product_price']
            quantity = request.POST['quantity']
            product_weight = request.POST['product_weight']
            product_description = request.POST['product_description']
            image1 = request.FILES.get('image1')
            image2 = request.FILES.get('image2')
            image3 = request.FILES.get('image3')
            if Products.objects.filter(product_id=product_id).exists():
                print('product already exists')
                return JsonResponse('false1', safe=False)
            elif Products.objects.filter(product_name=product_name).exists():
                print('This product name is already taken')
                return JsonResponse('false2', safe=False)
            else:
                print('heyyy')
                obj_category = Category.objects.get(id=product_categorie)
                Products.objects.create(product_id=product_id, product_name=product_name,category=obj_category, 
                                        product_price=product_price, product_quantity=quantity,product_weight=product_weight,
                                         product_description=product_description, image1=image1, image2=image2, image3=image3)
                return JsonResponse('true', safe=False)

        context = {
            'categorys': category
        }
        return render(request, 'vendor/add-product.html', context)

    else:
        return redirect('ve-login')
