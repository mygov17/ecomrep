from django.db import models
import datetime
from django.db.models.deletion import CASCADE
# Create your models here.

class Category(models.Model): # categoty iof products
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Customer(models.Model): #customer self
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='uploads/product/')
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    discription = models.CharField(max_length=250)
    created_at = models.DateField(default=datetime.datetime.today)
    is_price = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=6, decimal_places= 2)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    status = models.BooleanField(default=False)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return str(self.product)