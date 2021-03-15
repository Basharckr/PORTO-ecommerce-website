from django.shortcuts import render, redirect
from django.http import JsonResponse, response
from django.contrib.auth.models import User, auth
from .models import Products
# from django.core.files import File
from owner.models import Category
from django.contrib.auth import logout
from django.contrib import messages


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
        product = Products.objects.all()
        # print(product.image1)
        context = {
            'products': product
        }
        return render(request, 'vendor/manage-product.html', context)
    else:
        return redirect('ve-login')


def add_product(request):
    if request.user.is_authenticated and request.user.is_staff == True:
        category = Category.objects.all()

        if request.method == 'POST':
            product_id = request.POST['product_id']
            product_name = request.POST['product_name']
            product_categorie = request.POST['product_categorie']
            product_price = request.POST['product_price']
            quantity = request.POST['quantity']
            product_weight = request.POST['product_weight']
            product_description = request.POST['product_description']
            image1 = request.FILES.get('image1')
            image2 = request.FILES.get('image2')
            image3 = request.FILES.get('image3')
            print(image1)
            if Products.objects.filter(product_id=product_id).exists():
                print('product already exists')
                # return JsonResponse('false1', safe=False)
                pass
            elif Products.objects.filter(product_name=product_name).exists():
                print('This product name is already taken')
                # return JsonResponse('false2', safe=False)
                pass
            else:

                obj_category = Category.objects.get(id=product_categorie)
                Products.objects.create(product_id=product_id, product_name=product_name, category=obj_category,
                                        product_price=product_price, product_quantity=quantity, product_weight=product_weight,
                                        proudct_description=product_description, image1=image1, image2=image2, image3=image3)
                print('product added successfully')
                messages.success(request, 'Product added successfully')
                return redirect('add-product')

        context = {
            'categorys': category
        }
        return render(request, 'vendor/add-product.html', context)

    else:
        return redirect('ve-login')


def edit_product(request, pk):
    if request.user.is_authenticated and request.user.is_staff == True:
        edit = Products.objects.get(id=pk)
        if request.method == 'POST':
            edit.product_id = request.POST['product_id']
            edit.product_name = request.POST['product_name']
            edit.product_categorie = request.POST['product_categorie']
            edit.product_price = request.POST['product_price']
            edit.quantity = request.POST['quantity']
            edit.product_weight = request.POST['product_weight']
            edit.product_description = request.POST['product_description']
            edit.image1 = request.FILES.get('image1')
            edit.image2 = request.FILES.get('image2')
            edit.image3 = request.FILES.get('image3')
            if Products.objects.filter(product_id=edit.product_id, product_name=edit.product_name).exclude(id=pk).exists():
                print('this product already exist')
            else:
                edit.save()
                print('the product successfully updated')
                return redirect('manage-product')
        category = Category.objects.all()
        context = {
            'products': edit, 'category': category,
        }
        return render(request, 'vendor/edit-product.html', context)

    else:
        return redirect('ve-login')


def delete_product(request, pk):
    if request.user.is_authenticated and request.user.is_staff == True:

        del_product = Products.objects.get(id=pk)
        del_product.delete()
        return redirect('manage-product')

    else:
        return redirect('ve-login')


def block_unblock_product(request, pk):
    if request.user.is_authenticated and request.user.is_staff == True:
        product = Products.objects.get(id=pk)
        if product.product_value == True:
            product.product_value = False
            print('vendor is blocked')
        else:
            product.product_value = True
            print('vendor is unblocked')
        product.save()

        return redirect('manage-product')

    else:
        return redirect('ad-login')
