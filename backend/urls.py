from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include, url
from chatbox import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^chatbox/', include('chatbox.urls')),
    url(r'^admin/', admin.site.urls),
]

 
