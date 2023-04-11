from django.contrib import admin
from .models import Product
# Register your models here.

admin.site.site_header = 'Buy & Sell Website'
admin.site.site_title = 'Product & Seller Managament Dashboard'
admin.site.index_title = 'Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc']
    search_fields = ('name',)
    list_editable = ['price', 'desc']
    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)
    actions= ('set_price_to_zero',)
admin.site.register(Product,ProductAdmin)