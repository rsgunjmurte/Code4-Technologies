from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 50)
    description = models.TextField(blank = True,)
    created_date = models.DateField()
    updated_date = models.DateField(blank = True, null = True)

    def __str__(self):
        return self.category_name

    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(blank = True,)
    product_price = models.IntegerField()
    stock_quantity = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.product_name