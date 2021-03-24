from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import JsonResponse, response
from django.contrib.auth import logout
from vendor.models import Products
from .models import Cart, ShipAddress, Order
from django.views.decorators.csrf import csrf_exempt

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
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.is_active:        
                    user = auth.authenticate(username=username, password=password)
                    if user is not None:     
                        print('goto user home')
                        auth.login(request, user)
                        return JsonResponse('true', safe=False)             
                    else:
                        print("incorrect password")
                        return JsonResponse('false', safe=False)
                else:
                    return JsonResponse('blocked', safe=False)
            else:
                return JsonResponse('nouser', safe=False) 
        return render(request, 'myapp/login.html')
    return render(request, 'myapp/login.html')

def signup(request):
    if request.method == 'POST':
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
            user = User.objects.create_user(
                first_name=firstname, last_name=lastname, username=username, email=email, password=password)
            print('user is created')
            return JsonResponse('true', safe=False)
    return render(request, 'myapp/signup.html')


def landing(request):
    if request.user.is_authenticated:
        product = Products.objects.filter(product_value=True)
        context = {
            'products': product
        }
        return render(request, 'myapp/landing.html', context)
    else:
        return redirect("login")


def userlogout(request):
    logout(request)
    return redirect('login')


def product(request, pk):
    if request.user.is_authenticated:
        product = Products.objects.get(id=pk)
        context = {
            'products': product
        }
        return render(request, 'myapp/product_detail.html', context)
    else:
        return redirect("login")

def user_cart(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            total = 0.00
            for item in cart:
                total = total + int(item.user_product.product_price) * int(item.product_count)
            tot = []
            tot.append(total)
            request.session['total'] = tot
            context = {
                'cart': cart, 'grant': tot
            }
            return render(request, 'myapp/cart.html', context)
        else:
            return redirect('login')
    else:
        return redirect("login")

@csrf_exempt
def add_to_cart(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            if request.method == 'POST':
                count = request.POST['count']
                obj_product = Products.objects.get(id=id)
                if Cart.objects.filter(user_product=obj_product, user=request.user, checkedout=False).exists():
                    add = Cart.objects.get(user_product=obj_product)           
                    add.product_count = add.product_count + int(count)
                    add.save()
                    return JsonResponse('true', safe=False)
                else:
                    cart = Cart.objects.create(user_product=obj_product, user=request.user, product_count=count)
                    return JsonResponse('true', safe=False)
            else:
                return JsonResponse('false', safe=False)
        else:
            return redirect('login')
    else:
        return redirect("login")

def remove_from_cart(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            product = Cart.objects.get(id=id)
            product.delete()
            return JsonResponse('true', safe=False) 
        else:
            return redirect('login')
    else:
        return redirect("login")

def clear_all_cart(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            product = Cart.objects.filter(user=request.user, checkedout=False)
            print(product)
            product.delete()

            return redirect('cart')
        else:
            return redirect('login')
    else:
        return redirect("login")

@csrf_exempt
def edit_quantity(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            quantity = request.POST['quantity']
            print(quantity)
            edit = Cart.objects.get(id=id)
            print(edit)
            if edit.product_count == quantity:
                print(edit.product_count)
                print(quantity)
                return JsonResponse('nothing', safe=False)
            else:
                edit.product_count = quantity
                edit.save()
                return JsonResponse('true', safe=False) 
        else:
            return redirect('login')
    else:
        return redirect("login")

def checkout(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:                
            address = ShipAddress.objects.filter(user=request.user)
            print(address)
            context = {
                'address': address
            }
            return render(request, 'myapp/checkout.html', context)
        else:
            return redirect('login')
    else:
        return redirect("login")

def add_address(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            if request.method == 'POST':
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                organization = request.POST['organization']
                street = request.POST['street']
                city = request.POST['city']
                state = request.POST['state']
                pincode = request.POST['pincode']
                country = request.POST['country']
                number = request.POST['number']
                ShipAddress.objects.create(user=request.user, firstname=firstname, lastname=lastname,
                                           organization=organization, streetaddress=street, city=city,
                                           state=state, pincode=pincode, country=country, number=number)          
                return JsonResponse('true', safe=False)
            else:  
                return JsonResponse('false', safe=False)
        else:
            return redirect('login')
    else:
        return redirect("login")

def edit_address(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            if request.method == 'POST':                
                address = ShipAddress.objects.filter(user=request.user, id=id)
                address.firstname = request.POST['firstname1']
                address.lastname = request.POST['lastname1']
                address.organization = request.POST['organization1']
                address.street = request.POST['street1']
                address.city = request.POST['city1']
                address.state = request.POST['state1']
                address.pincode = request.POST['pincode1']
                address.country = request.POST['country1']
                address.number = request.POST['number1']
                address.save()
                return JsonResponse('true', safe=False)
            else:
                return JsonResponse('false', safe=False)
        else:
            return redirect('login')
    else:
        return redirect("login")

def delete_address(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            address = ShipAddress.objects.get(id=id)
            address.delete()
            return redirect('checkout')      
        else:
            return redirect('login')
    else:
        return redirect("login")



@csrf_exempt
def set_address(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            request.session['address-id'] = id

            return JsonResponse('true', safe=False)
        else:
            return redirect('login')
    else:
        return redirect("login")

def placeorder(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            total = request.session['total']                  
            id = request.session['address-id']
            address = ShipAddress.objects.get(id=id)
                
            return render(request, 'myapp/placeorder.html', {'address':address, 'grant_total':total})
        else:
            return redirect('login')
    else:
        return redirect("login")


def success(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:                
            return render(request, 'myapp/success.html')
        else:
            return redirect('login')
    else:
        return redirect("login")


@csrf_exempt
def order(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            id = request.session['address-id']
            print(id)
            grant_total = request.session['total']
            print(grant_total)
            cart = Cart.objects.filter(user=request.user, checkedout=False)
            print(cart)
            ship_id = ShipAddress.objects.get(id=id)
            if request.method == 'POST':
                for item in cart:
                    Order.objects.create(user=request.user, user_cart=item,
                                        quantity=item.product_count, amount=item.user_product.product_price, 
                                        ship_id=ship_id, payment_status=False)
                    item.checkedout=True
                    item.save()   
                return JsonResponse('cod', safe=False)
            else:
                for item in cart:
                    Order.objects.create(user=request.user, user_cart=item,
                                        quantity=item.product_count, amount=item.user_product.product_price, 
                                        ship_id=ship_id, payment_status=True)
                    item.checkedout=True
                    item.save()                      
                return JsonResponse('true', safe=False)                 
        else:
            return redirect('login')
    else:
        return redirect("login")


def dashbaord(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
           
                
            return render(request, 'myapp/dashboard.html')
        else:
            return redirect('login')
    else:
        return redirect("login")
