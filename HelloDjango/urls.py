"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from HelloDjango.view import hello
from HelloDjango.view import testdb
from HelloDjango.view import add
from HelloDjango.view import weather
from django.contrib import admin

urlpatterns = [
		
    url(r'^hello/$', hello), #Django V1.10 没有patterns，使用url，r'^hello/$'匹配192.168.1.38:8000/hello/
    url(r'^add/(\d+)/(\d+)$', add, name = 'add'),
    url(r'^$',hello),
    url(r'^admin/', admin.site.urls),
    url(r'^testdb/$', testdb),
    url(r'^weather/(\w+)?$', weather, name = 'weather'),
]
