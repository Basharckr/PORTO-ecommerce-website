from django.urls import path
from vendor import views


urlpatterns = [

    path('', views.index, name='ve-index'),
    

]