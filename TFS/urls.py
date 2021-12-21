from django.contrib import admin
from django.urls import path, include
from TFS import views

urlpatterns = [
    path('',views.Home, name="Home"),
    path('customers',views.customers, name="customers"),
    path('trans',views.trans, name="trans"),
]
