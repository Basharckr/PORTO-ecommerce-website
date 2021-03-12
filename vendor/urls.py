from django.urls import path
from vendor import views


urlpatterns = [

    path('', views.veIndex, name='ve-index'),
    path('login', views.veLogin, name='ve-login'),
    path('signup', views.veSignup, name='ve-signup'),
    path('logout', views.veLogout, name='ve-logout'),
    path('add-product', views.create_product, name='add-product'),
    path('manage-product', views.manage_product, name='manage-product'),


    

    

]