"""telkos2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from Post import views

urlpatterns = [
	url(r'^$', views.userlogin),
    url(r'^register/', views.user_register),
    url(r'^admin/', admin.site.urls),
    url(r'^list/', views.post_list, name = "list"),
    url(r'^create/', views.post_create),
    url(r'^edit/(?P<id>\d+)/$', views.post_update),
    url(r'^detail/(?P<id>\d+)/$', views.post_detail, name = "detail"),
    url(r'^delete/(?P<id>\d+)/$', views.post_delete),
    url(r'^logout/', views.post_logout),
]