from django.urls import path
from owner import views


urlpatterns = [

    path('', views.adIndex, name='ad-index'),
    path('login', views.adLogin, name='ad-login'),
    path('logout', views.adLogout, name='ad-logout'),
    path('create-category', views.create_category, name='create-category'),
    path('manage-category', views.manage_category, name='manage-category'),
    path('edit-category/<int:pk>/', views.edit_category, name='edit-category'),
    path('delete-category/<int:pk>/', views.delete_category, name='delete-category'),
    path('manage-vendor', views.manage_vendor, name='manage-vendor'),
    path('delete-vendor/<int:pk>/', views.delete_vendor, name='delete-vendor'),
    path('block-unblock-vendor/<int:pk>/', views.block_unblock_vendor, name='block-unblock-vendor'),
    # path('unblock-vendor/<int:pk>/', views.unblock_vendor, name='unblock-vendor'),








    
]