from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    prepopulated_fields = {"description": ("name",)}  # Automatically generate descriptions based on the name
