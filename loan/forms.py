from django import forms
from .models import Loan, Item, Customer
from django.forms.widgets import DateInput


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ('customer', 'item', 'quantity' , 'starting_date'  , 'ending_date')
        widgets = {
            'starting_date': DateInput(attrs={'type': 'date'}),
            'ending_date': DateInput(attrs={'type': 'date'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_email', 'customer_phone_number' , "customer_address"]
