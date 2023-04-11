from django.urls import path
from .views import (loan_list, dashboard, items, customer, 
                    loan_create, item_create, customer_create, 
                    loan_detail, loan_update, loan_delete , customer_detail , customer_loan)

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("loan_create/", loan_create, name="loan_create"),
    path("item_create/", item_create, name="item_create"),
    path("customer_create/", customer_create, name="customer_create"),
    path("items/", items, name="items"),
    path('customers/<int:pk>/', customer_detail, name='customer_detail'),
    path("customer/", customer, name="customer"),
    path('loans/', loan_list, name='loan_list'),
    path('customer_loan/<int:pk>/', customer_loan , name="customer_loan"),
    path('loans/<int:pk>/', loan_detail, name='loan_detail'),
    path('loans/<int:pk>/update/', loan_update, name='loan_update'),
    path('loans/<int:pk>/delete/', loan_delete, name='loan_delete'),
]
