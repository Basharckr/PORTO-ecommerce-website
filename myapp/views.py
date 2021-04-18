import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import JsonResponse, response
from django.contrib.auth import logout
from vendor.models import Products
from .models import Cart, ShipAddress, Order, Profile
from owner.models import Category, Coupons
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from twilio.rest import Client
import base64
from django.core.files.base import ContentFile
import string
import random
from django.core import serializers



# Create your views here.


# Guest user view
def guest(request):
    if request.user.is_authenticated:
        return redirect("landing")
    else:
        product = Products.objects.filter(product_value=True)[:12]
        cart = Cart.objects.filter(user=request.user.id, checkedout=False)
        count = Cart.objects.filter(
            user=request.user.id, checkedout=False).count()
        brands = User.objects.filter(is_active=True, is_staff=True)
        category = Category.objects.all()
        context = {
            'products': product, 'cart': cart, 'count': count, 'category': category, 'brands': brands
        }
    return render(request, 'myapp/index.html', context)

# Login view
def login(request):
    if request.user.is_authenticated:
        return redirect("landing")
    else:
        product = Products.objects.filter(product_value=True)
        cart = Cart.objects.filter(user=request.user.id, checkedout=False)
        count = Cart.objects.filter(
            user=request.user.id, checkedout=False).count()
        brands = User.objects.filter(is_active=True, is_staff=True)
        category = Category.objects.all()
        context = {
            'products': product, 'cart': cart, 'count': count, 'category': category, 'brands': brands
        }
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.is_active:
                    user = auth.authenticate(
                        username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        return JsonResponse('true', safe=False)
                    else:
                        return JsonResponse('false', safe=False)
                else:
                    return JsonResponse('blocked', safe=False)
            else:
                return JsonResponse('nouser', safe=False)
        return render(request, 'myapp/login.html', context)
    return render(request, 'myapp/login.html', context)


phone_number = 0
otp = 0


# Otp login
def otp_login(request):
    if request.user.is_authenticated:
        return redirect("landing")
    else:
        product = Products.objects.filter(product_value=True)
        cart = Cart.objects.filter(user=request.user.id, checkedout=False)
        count = Cart.objects.filter(
            user=request.user.id, checkedout=False).count()
        brands = User.objects.filter(is_active=True, is_staff=True)
        category = Category.objects.all()
   
        context = {
            'products': product, 'cart': cart, 'count': count, 'category': category, 'brands': brands
        }
        if request.method == 'POST':
            global phone_number
            phone_number = request.POST['number']
            if Profile.objects.filter(phone=phone_number).exists():
                user = Profile.objects.get(phone=phone_number)
                if user.user.is_active:
                    random_num = random.randint(1000, 9999)
                    global otp
                    otp = random_num
                    account_sid = 'AC52079fbfb832168a7dbb21afde88c1bf'
                    auth_token = '8f5895e649cb4274d6878de3661fb989'
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                        body=f"Your OTP is {otp}",
                        from_='+12064881795',
                        to=f"+919846337553"
                    )
                    return JsonResponse('true', safe=False)
                else:
                    return JsonResponse('blocked', safe=False)
            else:
                return JsonResponse('nouser', safe=False)
    return render(request, 'myapp/otp-login.html', context)



def enter_otp(request):
    if request.method == 'POST':
        otp1 = request.POST['otp']
        global phone_number
        user = Profile.objects.get(phone=phone_number)
        thisuser = user.user
        global otp
        if int(otp1) == otp:
            auth.login(request, thisuser)
            return JsonResponse('true', safe=False)
        else:
            return JsonResponse('false', safe=False)
    else:
        return render(request, 'myapp/enter-otp.html')


def signup(request):
    product = Products.objects.filter(product_value=True)
    cart = Cart.objects.filter(user=request.user.id, checkedout=False)
    count = Cart.objects.filter(
        user=request.user.id, checkedout=False).count()
    brands = User.objects.filter(is_active=True, is_staff=True)
    category = Category.objects.all()

    context = {
        'products': product, 'cart': cart, 'count': count, 'category': category, 'brands': brands
    }
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        number = request.POST['number']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse('false1', safe=False)
        if User.objects.filter(email=email).exists():
            return JsonResponse('false2', safe=False)
        if Profile.objects.filter(phone=number).exists():
            return JsonResponse('false3', safe=False)
        else:
            user = User.objects.create_user(
                first_name=firstname, last_name=lastname, username=username, email=email, password=password)
            Profile.objects.create(user=user, phone=number)
            coupon_code = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 7))
            Coupons.objects.create(coupon_code=coupon_code, coupon_offer=30, user=user)

            return JsonResponse('true', safe=False)
    return render(request, 'myapp/signup.html', context)


def landing(request):
    if request.user.is_authenticated:
        product = Products.objects.filter(product_value=True)[:12]
        cart = Cart.objects.filter(user=request.user.id, checkedout=False)
        count = Cart.objects.filter(
            user=request.user.id, checkedout=False).count()
        brands = User.objects.filter(is_active=True, is_staff=True)
        category = Category.objects.all()
        total = 0.00
        for item in cart:
            total = total + \
                int(item.user_product.offer_price) * \
                int(item.product_count)
        tot = []
        tot.append(total)
        request.session['total'] = tot
        context = {
            'products': product, 'cart': cart, 'grant': tot, 'count': count, 'category': category, 'brands': brands
        }
        return render(request, 'myapp/landing.html', context)
    else:
        return redirect("guest")


def userlogout(request):
    logout(request)
    return redirect('login')


def product(request, pk):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            product = Products.objects.get(id=pk)
            related_product = Products.objects.filter(
                category=product.category).exclude(id=pk)
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            category = Category.objects.all()
            brands = User.objects.filter(is_active=True, is_staff=True)
            tot = request.session['total']
            context = {
                'products': product, 'cart': cart, 'grant': tot, 'count': count, 'category': category,
                'brands': brands, 'related_product': related_product
            }
            return render(request, 'myapp/product_detail.html', context)
        else:
            return redirect("login")
    else:
        return redirect("login")





def user_cart(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:    
            cart = Cart.objects.filter(
                user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            category = Category.objects.all()
            brands = User.objects.filter(is_active=True, is_staff=True)

            total = 0.00
            for item in cart:
                total = total + \
                    int(item.user_product.offer_price) * \
                    int(item.product_count)
            tot = []
            tot.append(total)
            subtotal = tot[0]
            request.session['total'] = tot

            context = {
                'cart': cart, 'grant': tot, 'count': count, 'category': category, 'brands': brands,  'subtotal': subtotal
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
                if obj_product.product_quantity >= int(count):
                    if Cart.objects.filter(user_product=obj_product, user=request.user, checkedout=False).exists():
                        try:
                            add = Cart.objects.get(user_product=obj_product)
                            add.product_count = add.product_count + int(count)
                            add.save()
                            return JsonResponse('true', safe=False)
                        except:
                            return JsonResponse('cart', safe=False)

                    else:
                        cart = Cart.objects.create(
                            user_product=obj_product, user=request.user, product_count=count)
                        return JsonResponse('true', safe=False)
                else:
                    return JsonResponse('outstock', safe=False)
            else:
                return JsonResponse('false', safe=False)
        else:
            return redirect('login')
    else:
        return JsonResponse('notuser', safe=False)


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
            edit = Cart.objects.get(id=id)
            if edit.user_product.product_quantity >= int(quantity):
                if edit.product_count == quantity:
                    return JsonResponse('nothing', safe=False)
                else:
                    edit.product_count = quantity
                    edit.save()
                    return JsonResponse('true', safe=False)
            else:
                return JsonResponse('outstock', safe=False)
        else:
            return redirect('login')
    else:
        return redirect("login")


def checkout(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            address = ShipAddress.objects.filter(user=request.user)
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            category = Category.objects.all()
            brands = User.objects.filter(is_active=True, is_staff=True)
            
            if request.method == 'POST':
                coupon_code = request.POST['coupon_code']
                cart = Cart.objects.filter(
                    user=request.user.id, checkedout=False)
                if Coupons.objects.filter(coupon_code=coupon_code, active=False).exists():
                    coupon_offer = Coupons.objects.get(
                        coupon_code=coupon_code, active=False)
                    total = request.session['total']
                    discount_price = []
                    discount_price.append(coupon_offer.coupon_offer)
                    deduct = []      
                    deduct.append(total[0] - discount_price[0])
                    request.session['total'] = deduct
                    coupon_offer.active = True
                    coupon_offer.save()
                    data = {
                        'discount_price': discount_price
                    }
                    return JsonResponse(data)
                else:

                    return JsonResponse('false', safe=False)
         
            tot = request.session['total']
            context = {
                'address': address, 'cart': cart, 'grant': tot, 'count': count, 'category': category, 'brands': brands,
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
                check = request.POST['check']
                data = ShipAddress.objects.filter(
                    select=True, user=request.user)
                if check == '1':
                    for item in data:
                        item.select = False
                        item.save()
                    ShipAddress.objects.create(user=request.user, firstname=firstname, lastname=lastname,
                                               organization=organization, streetaddress=street, city=city,
                                               state=state, pincode=pincode, country=country, number=number, select=True)
                else:
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
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            category = Category.objects.all()
            brands = User.objects.filter(is_active=True, is_staff=True)

            tot = request.session['total']
            
            return render(request, 'myapp/placeorder.html', {'address': address, 'grant': tot, 'cart': cart, 'count': count, 'category': category, 'brands': brands})
        else:
            return redirect('login')
    else:
        return redirect("login")


def success(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            category = Category.objects.all()
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            brands = User.objects.filter(is_active=True, is_staff=True)

            tot = request.session['total']

            context = {
                'category': category, 'brands': brands, 'grant': tot, 'cart': cart, 'count': count,
            }
            return render(request, 'myapp/success.html', context)
        else:
            return redirect('login')
    else:
        return redirect("login")


@csrf_exempt
def place_order(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            
            id = request.session['address-id']
            grant_total = request.session['total']
            cart = Cart.objects.filter(user=request.user, checkedout=False)
            ship_id = ShipAddress.objects.get(id=id)
            if request.method == 'POST':
                for item in cart:
                    if item.user_product.product_quantity >= item.product_count:
                        Order.objects.create(user=request.user, user_cart=item,
                                            quantity=item.product_count, amount=item.user_product.offer_price,
                                            ship_id=ship_id, payment_status=True)
                        item.checkedout = True
                        item.user_product.product_quantity -= item.product_count
                        item.user_product.save()
                        item.save()
                        del request.session['total']
                        return JsonResponse('true', safe=False)
                    else:
                        return JsonResponse('false', safe=False)

            else:
                for item in cart:
                    Order.objects.create(user=request.user, user_cart=item,
                                         quantity=item.product_count, amount=item.user_product.offer_price,
                                         ship_id=ship_id, payment_status=False)
                    item.checkedout = True
                   
                    item.user_product.product_quantity -= item.product_count
                    item.user_product.save()
                    item.save()
                    del request.session['total']
                return JsonResponse('cod', safe=False)

        else:
            return redirect('login')
    else:
        return redirect("login")


def dashbaord(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user.id)
            coupon = Coupons.objects.filter(user=request.user.id, active=False)
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            category = Category.objects.all()
            brands = User.objects.filter(is_active=True, is_staff=True)
            address = ShipAddress.objects.filter(
                select=True, user=request.user)

            tot = request.session['total']
            return render(request, 'myapp/dashboard.html', {'profile': profile, 'cart': cart, 'grant': tot, 'count': count,
                                                            'category': category, 'brands': brands, 'address': address, 'coupon': coupon})
        else:
            return redirect('login')
    else:
        return redirect("login")


def edit_user_account(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            category = Category.objects.all()
            brands = User.objects.filter(is_active=True, is_staff=True)

            tot = request.session['total']
            profile = Profile.objects.get(user=request.user.id)
            edit = User.objects.get(id=request.user.id)
            if request.method == 'POST':
                edit.firstname = request.POST['firstname']
                edit.lastname = request.POST['lastname']
                edit.username = request.POST['username']
                edit.email = request.POST['email']
                profile.phone = request.POST['number']
                orginalpassword = request.POST['orginalpassword']
                image1 = request.POST['text']
                format, img1 = image1.split(';base64,')
                ext = format.split('/')[-1]
                profile.image1 = ContentFile(base64.b64decode(img1), name=edit.firstname+ '.' + ext)
                checkpassword = check_password(
                    orginalpassword, request.user.password)
                if checkpassword:
                    if User.objects.filter(username=edit.username).exclude(id=request.user.id).exists():
                        messages.error(
                            request, 'This username already taken!!')
                        return redirect('edit-user-account')
                    elif User.objects.filter(email=edit.email).exclude(id=request.user.id).exists():
                        messages.error(request, 'The email already taken!!')
                        return redirect('edit-user-account')
                    elif Profile.objects.filter(phone=profile.phone).exclude(user=request.user.id).exists():
                        messages.error(request, 'The phone number already taken!!')
                        return redirect('edit-user-account')
                    else:
                        edit.save()
                        profile.save()
                        messages.success(
                            request, 'Profile information updated..')
                        return redirect('edit-user-account')
                else:
                    messages.error(request, 'password is incorrect')
                    return redirect('edit-user-account')
            return render(request, 'myapp/edit-user-account.html', {'profile': profile, 'cart': cart, 'grant': tot, 'count': count, 'category': category, 'brands': brands})
        else:
            return redirect('login')
    else:
        return redirect("login")


def change_user_password(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            edit = User.objects.get(id=request.user.id)
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            category = Category.objects.all()
            brands = User.objects.filter(is_active=True, is_staff=True)
            address = ShipAddress.objects.filter(
                select=True, user=request.user)

            tot = request.session['total']

            context = {
                'cart': cart, 'grant': tot, 'count': count, 'category': category, 'brands': brands,
            }
            if request.method == 'POST':
                password = request.POST['password']
                orginalpassword = request.POST['orginalpassword']

                checkpassword = check_password(
                    orginalpassword, request.user.password)
                if checkpassword:
                    edit.password = make_password(password)
                    edit.save()
                    return JsonResponse('true', safe=False)
                else:
                    return JsonResponse('false', safe=False)
            return render(request, 'myapp/change-user-password.html', context)
        else:
            return redirect('login')
    else:
        return redirect("login")


def my_orders(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            all_orders = Order.objects.filter(user=request.user.id)
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            category = Category.objects.all()
            brands = User.objects.filter(is_active=True, is_staff=True)

            tot = request.session['total']

            return render(request, 'myapp/my-orders.html', {'orders': all_orders, 'cart': cart, 'grant': tot, 'count': count, 'category': category, 'brands': brands})
        else:
            return redirect('login')
    else:
        return redirect("login")


def cancel_order(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            del_order = Order.objects.get(id=id)
            del_order.delete()
            return JsonResponse('true', safe=False)
        else:
            return redirect('login')
    else:
        return redirect("login")


def search_product(request):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            if request.method == 'POST':
                q = request.POST['q']
                category = request.POST['cat']
                obj = Category.objects.get(category_name=category)
                product = Products.objects.filter(
                    product_name__icontains=q, category=obj.id)
                cart = Cart.objects.filter(
                    user=request.user.id, checkedout=False)
                count = Cart.objects.filter(
                    user=request.user.id, checkedout=False).count()
                category = Category.objects.all()
                brands = User.objects.filter(is_active=True, is_staff=True)

            tot = request.session['total']

            context = {
                'product': product, 'cart': cart, 'grant': tot, 'count': count, 'category': category, 'brands': brands
            }
            return render(request, 'myapp/search-product.html', context)
        else:
            return redirect('login')
    else:
        return redirect("login")


def categorywise(request, pk):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            category = Category.objects.all()
            brands = User.objects.filter(is_active=True, is_staff=True)
            products = Products.objects.filter(category=pk)

            tot = request.session['total']

            context = {
                'cart': cart, 'grant': tot, 'count': count, 'category': category, 'products': products, 'brands': brands
            }
            return render(request, 'myapp/categorywise.html', context)
        else:
            return redirect('login')
    else:
        return redirect("login")


def brandwise(request, pk):
    if request.user.is_active == True:
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user.id, checkedout=False)
            count = Cart.objects.filter(
                user=request.user.id, checkedout=False).count()
            category = Category.objects.all()
            brands = User.objects.filter(is_active=True, is_staff=True)
            products = Products.objects.filter(vendor=pk)

            tot = request.session['total']

            context = {
                'cart': cart, 'grant': tot, 'count': count, 'category': category, 'products': products, 'brands': brands
            }
            return render(request, 'myapp/brandwise.html', context)
        else:
            return redirect('login')
    else:
        return redirect("login")
