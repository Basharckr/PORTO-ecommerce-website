from django.urls import path
from myapp import views


urlpatterns = [

    # ==============================Geust===========================================

    path('', views.guest, name='guest'),

    # ==============================User===========================================

    path('landing', views.landing, name='landing'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.userlogout, name='logout'),

    #otp login 

    path('otp-login', views.otp_login, name='otp-login'),
    path('enter-otp', views.enter_otp, name='enter-otp'),


    # ==============================Product===========================================

    path('product/<int:pk>/', views.product, name='product'),

    # ==============================Cart===========================================

    path('cart', views.user_cart, name='cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove-from-cart'),
    path('clear-all-cart/', views.clear_all_cart, name='clear-all-cart'),
    path('edit-quantity/<int:id>/', views.edit_quantity, name='edit-quantity'),

    # ==============================Checkout===========================================

    path('checkout', views.checkout, name='checkout'),

    # ==============================Shipp Address===========================================
    
    path('add-address', views.add_address, name='add-address'),
    path('edit-address/<int:id>/', views.edit_address, name='edit-address'),
    path('delete-address/<int:id>/', views.delete_address, name='delete-address'),

    # ==============================Placeorder===========================================

    path('placeorder', views.placeorder, name='placeorder'),
    
    # ==============================Sett address===========================================

    path('set-address/<int:id>/', views.set_address, name='set-address'),
    
    # ==============================Payment success===========================================
    
    path('success', views.success, name='success'),

    # ==============================Order===========================================

    path('order', views.place_order, name='order'),
    path('my-orders', views.my_orders, name='my-orders'),
    path('cancel-order/<int:id>/', views.cancel_order, name='cancel-order'),



    # ==============================User dashboard===========================================

    path('dashboard', views.dashbaord, name='dashboard'),
    path('edit-user-account', views.edit_user_account, name='edit-user-account'),
    path('change-user-password', views.change_user_password, name='change-user-password'),

    # ==============================User dashboard===========================================

    path('search-product', views.search_product, name='search-product'),

    # =============================Cateogry-brand wise display====================================

    path('categorywise/<int:pk>/', views.categorywise, name='categorywise'),
    path('brandwise/<int:pk>/', views.brandwise, name='brandwise'),



]