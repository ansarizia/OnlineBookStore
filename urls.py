"""OnlineBookStore URL Configuration

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

from django.conf.urls import url
from . import views



urlpatterns = [
    # /BookStore/
    url(r'^$', views.index, name='index' ),

    # /BookStore/Book_id(21)
    url(r'^(?P<Book_id>[0-9]+)/$',views.BuyNow, name='BuyNow'),

    #/BookStore/Fiction
    url(r'^(?P<Genre>\w+)/$',views.Details,name='Details'),

    #/BookStore/add
    url(r'^add/(\d+)',views.add_to_cart,name='add_to_cart'),

    #/BookStore/Remove
    url(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),

    #/BookStore/cart
    url(r'^cart/', views.cart, name='cart'),

]
