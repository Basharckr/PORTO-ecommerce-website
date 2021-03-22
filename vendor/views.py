from django.shortcuts import render, redirect
from django.http import JsonResponse, response
from django.contrib.auth.models import User, auth
from .models import Products
# from django.core.files import File
from owner.models import Category
from myapp.models import Cart, ShipAddress, Order
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.

def veIndex(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            return render(request, 'vendor/ve-index.html')
    else: 
        print('helloo')    
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
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.is_active:        
                    user = auth.authenticate(username=username, password=password)
                    if user is not None:     
                        print('goto vendor home')
                        auth.login(request, user)
                        return JsonResponse('true', safe=False)             
                    else:
                        print("incorrect password")
                        return JsonResponse('false', safe=False)
                else:
                    return JsonResponse('blocked', safe=False)
            else:
                return JsonResponse('nouser', safe=False) 
        return render(request, 'vendor/ve-login.html')
    return render(request, 'vendor/ve-login.html')


def veLogout(request):
    logout(request)
    return redirect('ve-login')


def manage_product(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            product = Products.objects.filter(vendor=request.user)
            # print(product.image1)
            context = {
                'products': product
            }
            return render(request, 'vendor/manage-product.html', context)
        else:
            return redirect('ve-login')

    else:
        return redirect('ve-login')


def add_product(request):
    if request.user.is_active == True:
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
                obj_category = Category.objects.get(id=product_categorie)
                Products.objects.create(vendor=request.user, product_id=product_id, product_name=product_name, category=obj_category,
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
    else:
        return redirect('ve-login')


def edit_product(request, pk):
    if request.user.is_active == True:
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
                if Products.objects.filter(product_id=edit.product_id).exclude(id=pk).exists():
                    messages.error(request, 'This product ID already exist')
                    return redirect('edit-product', pk)
                if Products.objects.filter(product_name=edit.product_name).exclude(id=pk).exists():
                    messages.error(request, 'This product name already exist')
                    return redirect('edit-product', pk)
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

    else:
        return redirect('ve-login')


def delete_product(request, pk):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            del_product = Products.objects.get(id=pk)
            del_product.delete()
            return redirect('manage-product')
        else:
            return redirect('ve-login')
    else:
        return redirect('ve-login')


def block_unblock_product(request, pk):
    if request.user.is_active == True:
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
    else:
        return redirect('ad-login')


def check_poructname(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            product_name = request.GET.get('product_name', None)
            response = {
                'is_taken': Products.objects.filter(product_name__iexact=product_name).exists()
            }
            return JsonResponse(response)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')
def check_poruct_id(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            product_id = request.GET.get('product_id', None)
            response = {
                'is_taken': Products.objects.filter(product_id__iexact=product_id).exists()
            }
            return JsonResponse(response)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')
def vendor_orders(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            print(request.user.id)
            order = Order.objects.filter(user_cart__user_product__vendor=request.user.id)
            print(order)
            context = {
                'orders': order
            }
            return render(request, 'vendor/vendor-orders.html', context)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')

def ship_status(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            print(request.user.id)
            order = Order.objects.get(id=id)
            print(order)
            if order.shipped == False:
                order.shipped = True         
                order.save()
                return JsonResponse('shipped', safe=False)
            else:
                order.shipped = False
                order.save()
                return JsonResponse('ship', safe=False)
            return render(request, 'vendor/vendor-orders.html')
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')

def delete_orders(request, pk):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            print(request.user.id)
            order = Order.objects.get(id=pk)
            order.delete()
            return redirect('vendor-orders')
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')