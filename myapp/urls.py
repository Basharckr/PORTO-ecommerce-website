from django.urls import path
from myapp import views


urlpatterns = [

    # ==============================Geust===========================================

    path('', views.index, name='index'),

    # ==============================User===========================================

    path('landing', views.landing, name='landing'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.userlogout, name='logout'),

    # ==============================Product===========================================

    path('product/<int:pk>/', views.product, name='product'),

    # ==============================Product===========================================

    path('cart', views.user_cart, name='cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove-from-cart'),
    path('clear-all-cart/', views.clear_all_cart, name='clear-all-cart'),



    
]