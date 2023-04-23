"""
URL configuration for Puzzle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome,name='welcome'),
    path('admin',views.admin1,name='admin1'),
    path('adminoptions',views.adminoptions,name='adminoptions'),
    path('admin2',views.admin2,name='admin2'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('signin',views.signin,name='signin'),
    path('skillhunt',views.skillhunt,name='skillhunt'),
    path('s1',views.step1,name='step1'),
    path('s2',views.step2,name='step2'),
    path('s3',views.step3,name='step3'),
    path('s4',views.step4,name='step4'),
    path('s5',views.step5,name='step5'),
    path('cave',views.cave,name='cave'),
    path('s6',views.step6,name='step6'),
    path('s7',views.step7,name='step7'),
    path('lead',views.leaderboard,name='leaderboard')
]
