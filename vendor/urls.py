from django.urls import path
from vendor import views



urlpatterns = [

    path('', views.veIndex, name='ve-index'),
    path('login', views.veLogin, name='ve-login'),
    path('signup', views.veSignup, name='ve-signup'),
    path('logout', views.veLogout, name='ve-logout'),
    path('add-product', views.add_product, name='add-product'),
    path('manage-product', views.manage_product, name='manage-product'),
    path('edit-product/<int:pk>/', views.edit_product, name='edit-product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete-product'),
    path('block-unblock-product/<int:pk>/', views.block_unblock_product, name='block-unblock-product'),




   

] 
