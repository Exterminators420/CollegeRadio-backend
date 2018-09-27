<<<<<<< HEAD
<<<<<<< HEAD
 
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
 
]
=======


 
>>>>>>> parent of 7aa2c44... uninstalled alauth
=======
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
]

>>>>>>> parent of db76616... conflict fixed
