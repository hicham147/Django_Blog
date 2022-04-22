"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from register import views as v
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as signin_views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',v.register,name='blog-register'),
    path('profile/',v.profile,name='profile'),
    path('signin/',signin_views.LoginView.as_view(template_name='Users/login.html'),name='signIn'),
    path('Signout/',signin_views.LogoutView.as_view(template_name='Users/logout.html'),name='signout'),
    path('',include('Myapp.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
