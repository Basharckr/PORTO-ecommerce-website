from django.urls import path
from owner import views


urlpatterns = [
    
    # ==============================Owner===========================================

    path('', views.adIndex, name='ad-index'),
    path('login', views.adLogin, name='ad-login'),
    path('logout', views.adLogout, name='ad-logout'),

    # ==============================Category===========================================

    path('create-category', views.create_category, name='create-category'),
    path('manage-category', views.manage_category, name='manage-category'),
    path('edit-category/<int:pk>/', views.edit_category, name='edit-category'),
    path('delete-category/<int:pk>/', views.delete_category, name='delete-category'),

    # ==============================Vendor=============================================

    path('manage-vendor', views.manage_vendor, name='manage-vendor'),
    path('block-unblock-vendor/<int:pk>/', views.block_unblock_vendor, name='block-unblock-vendor'),
    path('delete-vendor/<int:pk>/', views.delete_vendor, name='delete-vendor'),

    # ==============================User=============================================

    path('manage-user', views.manage_user, name='manage-user'),
    path('block-unblock-user/<int:pk>/', views.block_unblock_user, name='block-unblock-user'),

    # =============================All orders=============================================

    path('all-orders', views.all_orders, name='all-orders'),

    # =============================Full report=============================================

    path('All-report', views.all_report, name='all-report'),

    # =============================Change offer validity=============================================

    path('change-offervalidity/<int:id>/', views.change_offer_validity, name='change-offervalidity'),


    # ============================== Coupon ===========================================

    path('add-coupon', views.add_coupon, name='add-coupon'),
    path('manage-coupon', views.manage_coupon, name='manage-coupon'),
    path('change-couponvalidity/<int:id>/', views.change_coupon_validity, name='change-couponvalidity'),
    path('edit-coupon/<int:id>/', views.edit_coupon, name='edit-coupon'),
    path('delete-coupon/<int:id>/', views.delete_coupon, name='delete-coupon'),

    
]