"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logindata/',views.logindata,name='logindata'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('query/<int:pk>/',views.query,name='query'),
    path('querydata/<int:pk>/',views.querydata,name='querydata'),
    path('allquery/<int:pk>/',views.allquery,name="allquery"),
    # path('edit/<int:id>/<int:pk>/',views.edit,name='edit'),
    # path('updatedata/<int:x>/<int:pk>/',views.updatedata,name='updatedata'),
    path('search/<int:pk>/',views.search,name='search')
 
   

    
]
