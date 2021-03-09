from django.urls import path
from owner import views


urlpatterns = [

    path('', views.index, name='ad-index'),


    
]