from django.shortcuts import render, redirect
from django.http import JsonResponse, response
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from .models import Category
from vendor.models import Products
from myapp.models import Cart, Order, ShipAddress

# Create your views here.


def adIndex(request):
    if request.user.is_authenticated and request.user.is_superuser == True:
        return render(request, 'owner/ad-index.html')
    else:
        return redirect('ad-login')


def adLogin(request):
    if request.user.is_authenticated and request.user.is_superuser == True:
        return redirect('ad-index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                print('goto admin home')
                auth.login(request, user)
                return JsonResponse('true', safe=False)
            else:
                print("incorrect username or password")
                return JsonResponse('false', safe=False)
        return render(request, 'owner/ad-login.html')

    return render(request, 'owner/ad-login.html')


def adLogout(request):
    logout(request)
    return redirect('ad-login')


def create_category(request):
    if request.user.is_authenticated and request.user.is_superuser == True:
        category = Category.objects.all()
        if request.method == 'POST':
            categoryname = request.POST['category']
            if Category.objects.filter(category_name=categoryname).exists():
                print('category already added')
                return JsonResponse('false', safe=False)
            else:
                print('category is added')
                Category.objects.create(category_name=categoryname)
                return JsonResponse('true', safe=False)

        return render(request, 'owner/create-category.html', {'category': category})
    else:
        return redirect('ad-login')


def manage_category(request):
    if request.user.is_authenticated and request.user.is_superuser == True:
        category = Category.objects.all()

        return render(request, 'owner/manage-category.html', {'category': category})

    else:
        return redirect('ad-login')


def edit_category(request, pk):
    if request.user.is_authenticated and request.user.is_superuser == True:
        edit = Category.objects.get(id=pk)
        if request.method == 'POST':
            edit.category_name = request.POST['cate']
            if Category.objects.filter(category_name=edit.category_name).exclude(id=pk).exists():
                print('category already taken')
                return JsonResponse('false', safe=False)
            else:
                edit.save()
                print('category is edited')
                return JsonResponse('true', safe=False)
        else:

            return render(request, 'owner/edit-category.html', {'category': edit})
    else:
        return redirect('ad-login')


def delete_category(request, pk):
    if request.user.is_authenticated and request.user.is_superuser == True:
        category = Category.objects.get(id=pk)
        category.delete()
        return redirect('manage-category')
    else:
        return redirect('ad-login')


def manage_vendor(request):
    if request.user.is_authenticated and request.user.is_superuser == True:
        vendor = User.objects.filter(is_staff=True, is_superuser=False)
        context = {
            'vendors': vendor,
        }
        return render(request, 'owner/manage-vendor.html', context)

    else:
        return redirect('ad-login')


def delete_vendor(request, pk):
    if request.user.is_authenticated and request.user.is_superuser == True:
        user = User.objects.get(id=pk)
        user.delete()
        return redirect('manage-vendor')
    else:
        return redirect('ad-login')


def block_unblock_vendor(request, pk):
    if request.user.is_authenticated and request.user.is_superuser == True:
        user = User.objects.get(id=pk)
        product = Products.objects.filter(vendor=pk)
        if user.is_active == True:
            user.is_active = False
            for product in product:
                product.product_value = False
                product.save()

            print('vendor is blocked')
        else:
            user.is_active = True
            for product in product:
                product.product_value = True
                product.save()
            print('vendor is unblocked')
        user.save()

        return redirect('manage-vendor')

    else:
        return redirect('ad-login')


def manage_user(request):
    if request.user.is_authenticated and request.user.is_superuser == True:
        user = User.objects.filter(is_staff=False, is_superuser=False)
        context = {
            'users': user,
        }
        return render(request, 'owner/manage-user.html', context)

    else:
        return redirect('ad-login')


def block_unblock_user(request, pk):
    if request.user.is_authenticated and request.user.is_superuser == True:
        user = User.objects.get(id=pk)
        if user.is_active == True:
            user.is_active = False
            print('user is blocked')
        else:
            user.is_active = True
            print('user is unblocked')
        user.save()

        return redirect('manage-user')

    else:
        return redirect('ad-login')


def all_orders(request):
    if request.user.is_authenticated and request.user.is_superuser == True:
        all_order = Order.objects.all()
        context = {
            'all_orders': all_order
        }
        return render(request, 'owner/all-orders.html', context)

    else:
        return redirect('ad-login')

