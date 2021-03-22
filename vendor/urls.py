from django.urls import path
from vendor import views



urlpatterns = [
    # ==============================Vendor===========================================

    path('', views.veIndex, name='ve-index'),
    path('login', views.veLogin, name='ve-login'),
    path('signup', views.veSignup, name='ve-signup'),
    path('logout', views.veLogout, name='ve-logout'),

    # ==============================Product===========================================

    path('manage-product', views.manage_product, name='manage-product'),
    path('add-product', views.add_product, name='add-product'),
    path('edit-product/<int:pk>/', views.edit_product, name='edit-product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete-product'),
    path('block-unblock-product/<int:pk>/', views.block_unblock_product, name='block-unblock-product'),

    # ==============================Check Product ID Name====================================

    path('check-product-name', views.check_poructname, name='check-product-name'),
    path('check-product-id', views.check_poruct_id, name='check-product-id'),

    # ==============================Order====================================

    path('vendor-orders', views.vendor_orders, name='vendor-orders'),
    path('delete-orders/<int:pk>/', views.delete_orders, name='delete-orders'),
    
    # ==============================Changin ship status====================================

    path('change-ship-status/<int:pk>/', views.ship_status, name='change-ship-status'),

   

] 
