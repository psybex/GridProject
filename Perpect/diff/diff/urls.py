"""diff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from home import views
from myaccount import views as accountviews
from grid import views as gridviews
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home, name = 'home'),
    path('', gridviews.grid, name='grid'),
    path('mygrid/<str:username>', gridviews.mygrid, name='mygrid'),
    path('detail/<str:key>', gridviews.detail, name='detail'),
    path('sign_up', accountviews.sign_up, name='sign_up'),
    #path('login', accountviews.login, name='login'),
    path('login/', LoginView.as_view(), name='login'),     # auth의 내장 함수 사용할 경우
    #path('logout', accountviews.logout, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('social_account', include('allauth.urls')),

    path('create', gridviews.create, name='create'),
    #path('update', gridviews.update, name='update'),
    #path('delete', gridviews.delete, name='delete'),
]
