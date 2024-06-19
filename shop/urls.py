from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('cart/', views.cart_view, name='cart'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('catalog/womens_dresses/', views.womens_dresses_view, name='womens_dresses'),
    path('catalog/womens_embroidery/', views.womens_embroidery_view, name='womens_embroidery'),
    path('catalog/childrens_dresses/', views.childrens_dresses_view, name='childrens_dresses'),
    path('catalog/childrens_embroidery/', views.childrens_embroidery_view, name='childrens_embroidery'),
]

urlpatterns += [
    path('logout/', LogoutView.as_view(), name='logout'),
]