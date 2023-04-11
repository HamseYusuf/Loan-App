from django.shortcuts import render, redirect, get_object_or_404
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

def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    loans = customer.loan_set.all()
    total_price = sum(loan.get_total_price() for loan in loans)
    
   
    
    context = {
        'customer': customer,
        'loans': loans,
        'total_price': total_price,
        
    }
    return render(request, 'loan/customer_detail.html', context)

def customer_loan(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.customer = customer
            loan.save()
            messages.success(request, 'Loan submitted successfully!')
            return redirect('customer_loan', pk=pk)
    else:
        form = LoanForm(initial={'customer': customer})
    context = {
        'customer': customer,
        'form': form
    }
    return render(request, 'loan/loan_form.html', context)



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


def loan_detail(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    context = {
        'loan': loan
    }
    return render(request, 'loan/loan_detail.html', context)


def loan_update(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    form = LoanForm(request.POST or None, instance=loan)
    if form.is_valid():
        form.save()
        messages.success(request, 'Loan updated successfully!')
        return redirect('loan_list')
    context = {
        'form': form
    }
    return render(request, 'loan/loan_form.html', context)


def loan_delete(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    if request.method == 'POST':
        loan.delete()
        messages.success(request, 'Loan deleted successfully!')
        return redirect('loan_list')
    context = {
        'loan': loan
    }
    return render(request, 'loan/loan_confirm_delete.html', context)
