"""envision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from backend import views
from . import urls
from rest_framework.routers import DefaultRouter,url
from django.views.generic import TemplateView

router=DefaultRouter()

router.register(r'UserViewSet',views.UserViewSet)


router.register(r'HealthViewSet',views.HealthViewSet)
router.register(r'ServiceViewSet',views.ServiceViewSet)
router.register(r'WaterViewSet',views.WaterViewSet)
router.register(r'NoticeViewSet',views.NoticeViewSet)




urlpatterns = [
    url('^api/',include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/',views.UserAPIView.as_view()),
    path('changepassword/',views.ChangePasswordAPIView.as_view()),


]
