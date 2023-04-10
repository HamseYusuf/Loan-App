from django.contrib import admin
from .models import Customer, Item, Loan

class LoanAdmin(admin.ModelAdmin):
    list_display = ('customer', 'item', 'quantity', 'starting_date', 'ending_date')

admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Loan, LoanAdmin)
