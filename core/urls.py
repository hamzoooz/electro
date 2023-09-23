from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('product/<int:id>', views.product_detials , name='product_detials'),
    path('store', views.store , name='store'),
    path('checkout', views.checkout , name='checkout'),
]
