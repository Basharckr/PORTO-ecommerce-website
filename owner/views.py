from django.shortcuts import render, redirect
from django.http import JsonResponse, response, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from .models import Category, Coupons
from vendor.models import Products
from myapp.models import Cart, Order, ShipAddress, Profile
from django.contrib import messages
import datetime
import xlwt

# Create your views here.


def adIndex(request):
    if request.user.is_authenticated and request.user.is_superuser == True:
        report_user = Profile.objects.filter(report=True)
        order = Order.objects.all()
        products = Products.objects.all().count()
        total_user = User.objects.filter(is_active=True, is_staff=False).count()
        total_vendors = User.objects.filter(is_active=True, is_staff=True, is_superuser=False).count()
        price = []
        date = []
        total = 0.00
        for item in order:
            total = total + item.order_total
            price.append(item.order_total)
            date.append(item.ordered_date.day)

        context = {
            'report': report_user, 'total': total, 'products': products, 'total_user': total_user,
            'total_vendors': total_vendors, 'date': date, 'price': price,
        }
        return render(request, 'owner/ad-index.html', context)
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
                auth.login(request, user)
                return JsonResponse('true', safe=False)
            else:
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
            category_offer = request.POST['offer']

            if Category.objects.filter(category_name=categoryname).exists():
                return JsonResponse('false', safe=False)
            else:
                Category.objects.create(category_name=categoryname, category_offer=category_offer)
                return JsonResponse('true', safe=False)

        return render(request, 'owner/create-category.html', {'category': category})
    else:
        return redirect('ad-login')

def change_offer_validity(request, id):
    if request.user.is_authenticated and request.user.is_superuser == True:
        category = Category.objects.get(id=id)
        if category.valid == False:
            category.valid = True
            category.save()
            return JsonResponse('true', safe=False)
        else:
            category.valid = False
            category.save() 
            return JsonResponse('false', safe=False)
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
            edit.category_offer = request.POST['offer']
            if Category.objects.filter(category_name=edit.category_name).exclude(id=pk).exists():
                return JsonResponse('false', safe=False)
            else:
                edit.save()
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

        else:
            user.is_active = True
            for product in product:
                product.product_value = True
                product.save()
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
        else:
            user.is_active = True
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

def all_report(request):
    if request.user.is_authenticated and request.user.is_superuser == True:
        if request.method == 'POST':
            start = request.POST['start']
            end = request.POST['end']
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename=Full_Report'+str(datetime.datetime.now()) +'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Full report')
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True

            columns = ['Username', 'Product', 'vendor_namwe', 'price', 'Quantity', 'Ordered date', 'Payment status', 'Shipping status']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)

            font_style = xlwt.XFStyle()
            rows = Order.objects.filter(ordered_date__range=[start, end]).values_list('user__username', 'user_cart__user_product__product_name',
                                                'user_cart__user_product__vendor__username',
                                                'amount', 'quantity', 'ordered_date', 'payment_status', 'shipped')
            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, str(row[col_num]), font_style)
            wb.save(response)
            return response
        else:
            all_order = Order.objects.all()
            context = {
                'all_orders': all_order
            }
        return render(request, 'owner/all-report.html', context)

    else:
        return redirect('ad-login')
 

def add_coupon(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_superuser == True:
            if request.method == 'POST':
                coupon_code = request.POST['couponcode']
                couponoffer = request.POST['couponoffer']
                if Coupons.objects.filter(coupon_code=coupon_code).exists():
                    return JsonResponse('false', safe=False)
                else:
                    Coupons.objects.create(coupon_code=coupon_code, coupon_offer=couponoffer)
                    messages.success(request, 'Coupon added successfully')
                    return JsonResponse('true', safe=False)
            coupons = Coupons.objects.all()
            context = {
                'coupons': coupons
            }
            return render(request, 'owner/add-coupon.html', context)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')

def manage_coupon(request):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_superuser == True:
            coupons = Coupons.objects.all()
            context = {
                'coupons': coupons
            }
            return render(request, 'owner/manage-coupon.html', context)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')


def change_coupon_validity(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_superuser == True:
            coupon = Coupons.objects.get(id=id)
            if coupon.active == False:
                coupon.active = True
                coupon.save()
                return JsonResponse('true', safe=False)
            else:
                coupon.active = False
                coupon.save() 
                return JsonResponse('false', safe=False)
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')


def edit_coupon(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_superuser == True:
            coupon = Coupons.objects.get(id=id)
            if request.method == 'POST':
                coupon.coupon_code = request.POST['couponcode']
                coupon.coupon_offer = request.POST['couponoffer']
                if Coupons.objects.filter(coupon_code=coupon.coupon_code).exclude(id=id).exists():
                    return JsonResponse('false', safe=False)
                else:
                    coupon.save()
                    messages.success(request, 'Changed successfully')
                    return JsonResponse('true', safe=False)
            return render(request, 'owner/edit-coupon.html', {'coupon': coupon})
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')


def delete_coupon(request, id):
    if request.user.is_active == True:
        if request.user.is_authenticated and request.user.is_superuser == True:
            coupon = Coupons.objects.get(id=id)
            coupon.delete()
            return redirect('manage-coupon')
        else:
            return redirect('ad-login')
    else:
        return redirect('ad-login')