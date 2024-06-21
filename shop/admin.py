from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'description')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    fields = ('name', 'description', 'price', 'category', 'image')
    list_per_page = 20

    # Дозволити видалення товару
    def delete_model(self, request, obj):
        obj.delete()

    # Дозволити видалення декількох товарів
    def delete_queryset(self, request, queryset):
        queryset.delete()

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    fields = ('name',)

    # Дозволити видалення категорії
    def delete_model(self, request, obj):
        obj.delete()

    # Дозволити видалення декількох категорій
    def delete_queryset(self, request, queryset):
        queryset.delete()
