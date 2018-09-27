 
from django.urls import path
from chat import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    path('chat/', views.home, name='index'),
    path('chat/chat1', views.chat, name='chat')
 
]
