from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('product', views.product_detials , name='product'),
    path('store', views.store , name='store'),
    path('checkout', views.checkout , name='checkout'),
]
