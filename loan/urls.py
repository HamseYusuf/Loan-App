from django.urls import path
from .views import loan_list , dashboard , items , customer , loan_create , item_create , customer_create

urlpatterns = [
    path("",dashboard, name="dashboard"),
    path("loan_create/",loan_create, name="loan_create"),
    path("item_create/",item_create, name="item_create"),
    path("customer_create/",customer_create, name="customer_create"),
    path("items/", items, name="items"),
    path("customer/", customer, name="customer"),
    path('loans/', loan_list, name='loan_list'),
]
