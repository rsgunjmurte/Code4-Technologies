from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'product_name', 'product_description', 'product_price', 'stock_quantity', 'created_at', 'updated_at']
admin.site.register(Product, ProductAdmin)  


class CatrgoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'description', 'created_date', 'updated_date']
admin.site.register(Category, CatrgoryAdmin)