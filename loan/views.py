from django.shortcuts import render, redirect
from .models import Loan, Item, Customer
from .forms import LoanForm, ItemForm, CustomerForm
from django.contrib import messages


def loan_list(request):
    loans = Loan.objects.all()
    context = {
        'loans': loans
    }
    return render(request, 'loan/loan_list.html', context)

def dashboard(request):
    return render(request, 'loan/dashboard.html')

def items(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'loan/items.html', context)

def customer(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'loan/customers.html', context)

def add_loan(request):
    form = LoanForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('loan_list')
    context = {
        'form': form
    }
    return render(request, 'loan/loan_form.html', context)

def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('items')
    context = {
        'form': form
    }
    return render(request, 'loan/item_form.html', context)

def customer_create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer')
    context = {
        'form': form
    }
    return render(request, 'loan/customer_form.html', context)


def loan_create(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save()
            messages.success(request, 'Loan submitted successfully!')
            return redirect('loan_create')
    else:
        form = LoanForm()

    context = {'form': form}
    return render(request, 'loan/loan_form.html', context)

