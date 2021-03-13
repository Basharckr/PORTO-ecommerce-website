from django.urls import path
from vendor import views
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [

    path('', views.veIndex, name='ve-index'),
    path('login', views.veLogin, name='ve-login'),
    path('signup', views.veSignup, name='ve-signup'),
    path('logout', views.veLogout, name='ve-logout'),
    path('add-product', views.add_product, name='add-product'),
    path('manage-product', views.manage_product, name='manage-product'),
   

] 
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 