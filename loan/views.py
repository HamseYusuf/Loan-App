from django.shortcuts import render, redirect
from .models import Loan, Item, Customer
from .forms import LoanForm, ItemForm, CustomerForm

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
        num_forms = int(request.POST.get('num_forms'))  # Get the number of forms submitted
        forms = [LoanForm(request.POST, prefix=str(i)) for i in range(num_forms)]

        if all([form.is_valid() for form in forms]):
            for form in forms:
                form.save()
            return redirect('loan_list')
    else:
        forms = [LoanForm(prefix=str(i)) for i in range(3)]  # Default to 3 blank forms

    context = {'forms': forms}
    return render(request, 'loan/loan_form.html', context)