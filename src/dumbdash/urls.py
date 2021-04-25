from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.orders_index, name='orders_index'),
    path("<int:pk>/", views.order_detail, name="order_detail"),
    path("create", views.order_create, name="order_create"),
    path("usersmodify", views.users_modify, name="users_modify"),
]
