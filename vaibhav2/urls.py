from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from products import views
from django.conf.urls.static  import static
import jobs.views
urlpatterns = [
    path('accounts/home',jobs.views.home,name='home'),
    path('admin/',admin.site.urls),
    path('accounts/blog/',include('blogs.urls')),
    path('accounts/',include('accounts.urls')),
    path('',views.homes,name='homes'),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
