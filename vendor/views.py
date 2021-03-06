from django.shortcuts import render, redirect
from django.http import JsonResponse, response, HttpResponse
from django.contrib.auth.models import User, auth
from .models import Products
from django.db.models import Sum
# from django.core.files import File
from owner.models import Category
from myapp.models import Cart, ShipAddress, Order, Profile
from django.contrib.auth import logout
from django.contrib import messages
import base64
from django.core.files.base import ContentFile
import datetime
import xlwt
from django.db.models.functions import TruncDate
from django.db.models import F
from django.db import models
import json
from django.core import serializers


# Create your views here.

def veIndex(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:

            data = Order.objects.filter(user_cart__user_product__vendor=request.user.id).order_by('ordered_date')
            products = Products.objects.filter(vendor=request.user).count()
            # data = Order.objects.filter(user_cart__user_product__vendor=request.user.id).annotate(date=TruncDate('ordered_date')).values('date').order_by('date').annotate(total_price=Sum(F('amount')*F('quantity'), output_field=models.FloatField()))
            
            total = 0
            orders = 0
            dist_users=set()
            date_price_dict = {}
            dates = []
            prices = []

            for item in data:
                price = item.amount * item.quantity
                date = item.ordered_date.date()
                total += price
                orders += 1

                dist_users.add(item.user)
                if date in date_price_dict.keys():
                    date_price_dict[date] += price
                else:
                    date_price_dict[date] = price

            count = len(dist_users)

            for date, price in date_price_dict.items():
                dates.append(str(date))
                prices.append(price)

            context = {
                'price': prices, 'date': dates, 'products': products, 'total': total, 'count': count, 'orders': orders
            }
            return render(request, 'vendor/ve-index.html', context)
    else: 
        return render(request, 'vendor/ve-login.html')


def veSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        number = request.POST['number']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse('false1', safe=False)
        elif User.objects.filter(email=email).exists():
            return JsonResponse('false2', safe=False)
        elif Profile.objects.filter(phone=number).exists():
            return JsonResponse('false3', safe=False)
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password, is_staff=True)
            Profile.objects.create(user=user, phone=number)
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
                        auth.login(request, user)
                        return JsonResponse('true', safe=False)             
                    else:
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
                image1 = request.POST['text']
                image2 = request.POST['text2']
                image3 = request.POST['text3']
                format, img1 = image1.split(';base64,')
                ext = format.split('/')[-1]
                pic1 = ContentFile(base64.b64decode(img1), name=product_name+ '.' + ext)
                format, img2 = image2.split(';base64,')
                pic2 = ContentFile(base64.b64decode(img2), name=product_name+ '.' + ext)
                format, img3 = image3.split(';base64,')
                pic3 = ContentFile(base64.b64decode(img3), name=product_name+ '.' + ext)
                obj_category = Category.objects.get(id=product_categorie)
                Products.objects.create(vendor=request.user, product_id=product_id, product_name=product_name, category=obj_category,
                                    product_price=product_price, product_quantity=quantity, product_weight=product_weight,
                                    proudct_description=product_description, image1=pic1, image2=pic2, image3=pic3)
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
                edit.product_quantity = request.POST['quantity']
                edit.product_weight = request.POST['product_weight']
                edit.product_description = request.POST['product_description']
                image1 = request.POST['text']
                image2 = request.POST['text2']
                image3 = request.POST['text3']
                format, img1 = image1.split(';base64,')
                ext = format.split('/')[-1]
                edit.image1 = ContentFile(base64.b64decode(img1), name=edit.product_name+ '.' + ext)
                format, img2 = image2.split(';base64,')
                edit.image2 = ContentFile(base64.b64decode(img2), name=edit.product_name+ '.' + ext)
                format, img3 = image3.split(';base64,')
                edit.image3 = ContentFile(base64.b64decode(img3), name=edit.product_name+ '.' + ext)
                if Products.objects.filter(product_id=edit.product_id).exclude(id=pk).exists():
                    messages.error(request, 'This product ID already exist')
                    return redirect('edit-product', pk)
                if Products.objects.filter(product_name=edit.product_name).exclude(id=pk).exists():
                    messages.error(request, 'This product name already exist')
                    return redirect('edit-product', pk)
                else:
                    edit.save()

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
            else:
                product.product_value = True
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
     
            order = Order.objects.filter(user_cart__user_product__vendor=request.user.id)
       
            context = {
                'orders': order
            }
            return render(request, 'vendor/vendor-orders.html', context)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')


def ship_status(request, pk):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            order = Order.objects.get(id=pk)
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
            order = Order.objects.get(id=pk)
            order.delete()
            return redirect('vendor-orders')
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')


def purchased_customers(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            customer = Order.objects.filter(user_cart__user_product__vendor=request.user.id)
            context = {
                'customer': customer
            }
            return render(request, 'vendor/customers.html', context)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')


def manage_customers(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            customer = Order.objects.filter(user_cart__user_product__vendor=request.user.id).distinct('user')
            context = {
                'customer': customer
            }
            return render(request, 'vendor/manage-customers.html', context)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')



def report_customer(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            user = Profile.objects.get(user=id)
            if request.method == 'POST':
                user.message = request.POST['message']
                user.report = True
                user.save()
                return JsonResponse('true', safe=False)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')


def vendor_report(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_staff == True:
            if request.method == 'POST':
                start = request.POST['start']
                end = request.POST['end']
                response = HttpResponse(content_type='application/ms-excel')
                response['Content-Disposition'] = 'attachment; filename=Report'+\
                    request.user.username+'_'+str(datetime.datetime.now()) +'.xls'
                wb = xlwt.Workbook(encoding='utf-8')
                ws = wb.add_sheet('Vendor report')
                row_num = 0
                font_style = xlwt.XFStyle()
                font_style.font.bold = True
                
                columns = ['Username', 'Product', 'Price', 'Quantity',  'Ordered date', 'Payment status', 'Shipping status']
                for col_num in range(len(columns)):
                    ws.write(row_num, col_num, columns[col_num], font_style)

                font_style = xlwt.XFStyle()
                rows = Order.objects.filter(user_cart__user_product__vendor=request.user.id, ordered_date__range=[start, end]).values_list('user__username', 'user_cart__user_product__product_name',
                                                                                                        'amount', 'quantity', 'ordered_date', 'payment_status',
                                                                                                        'shipped')
                for row in rows:
                    row_num += 1
                    for col_num in range(len(row)):
                        ws.write(row_num, col_num, str(row[col_num]), font_style)
                wb.save(response)
                return response
            else:
                order = Order.objects.filter(user_cart__user_product__vendor=request.user.id)
        
                context = {
                    'orders': order
                }
            return render(request, 'vendor/vendor-report.html', context)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')


def search_by_date(request):
    if request.method == 'GET':
        start = request.GET['start_date']
        end = request.GET['end_date']      
        order = Order.objects.filter(user_cart__user_product__vendor=request.user.id, ordered_date__range=[start, end]).only('user__username', 'user_cart__user_product__product_name',
                                                                                                        'amount', 'quantity', 'ordered_date', 'payment_status',
                                                                                                        'shipped')
        
        orders = serializers.serialize('json', order)
        return JsonResponse(orders, safe=False)
    
