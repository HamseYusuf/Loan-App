from django.db import models
from django.core.validators import MinValueValidator

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phone_number = models.PositiveIntegerField()
    customer_address = models.CharField(max_length=25)

    def __str__(self):
        return self.customer_name
    
class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.PositiveIntegerField()

class Loan(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    item = models.ForeignKey(Item , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    starting_date = models.DateField()
    ending_date = models.DateField()

    def duration(self):
        if self.end_date:
            return (self.end_date - self.start_date).days
        else:
            return None
        
    def total_price(self):
        return self.item.item_price * self.quantity

    def __str__(self):
        return f'{self.customer} - {self.item}'
