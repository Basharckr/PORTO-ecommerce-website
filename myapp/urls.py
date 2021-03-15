from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('landing', views.landing, name='landing'),
    path('logout', views.userlogout, name='logout'),
    path('product/<int:pk>/', views.product, name='product'),




    
]