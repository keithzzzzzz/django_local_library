"""bookclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url

from bookclubapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)$', views.user_detail.as_view()),
    url(r'^addresses/$', views.address_list),
    url(r'^addresses/(?P<pk>[0-9]+)$', views.address_detail.as_view()),
    url(r'^creditcards/$', views.creditcard_list),
    url(r'^creditcards/(?P<pk>[0-9]+)$', views.creditcard_detail.as_view()),
    url(r'^books/$', views.book_list),
    url(r'^books/(?P<pk>[0-9]+)$', views.book_detail),
    url(r'^booklists/$', views.booklist_list),
    url(r'^booklists/(?P<pk>[0-9]+)$', views.booklist_detail),
    url(r'^genres/$', views.genre_list),
    url(r'^genres/(?P<pk>[0-9]+)$', views.genre_detail),
    url(r'^genrelists/$', views.genrelist_list),
    url(r'^genrelists/(?P<pk>[0-9]+)$', views.delivery_detail),
    url(r'^deliveries/$', views.genrelist_list),
    url(r'^deliveries/(?P<pk>[0-9]+)$', views.delivery_detail),
]
