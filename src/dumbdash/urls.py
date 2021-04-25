from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.orders_index, name='orders'),
    path("orders/<int:pk>/", views.order_detail, name="order_detail"),
    path("new_order", views.order_create, name="order_create"),
    path("users", views.users_index, name="users"),
    path("users/<int:pk>", views.user_detail, name="user_detail"),
    path("restaurants", views.restaurants_index, name="restaurants"),
    path("restaurants/<int:pk>", views.restaurant_detail,
         name="restaurant_detail"),
]
