from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
<<<<<<< HEAD
    fields = ('name', 'image', 'descriprtion', ('price', 'quantity'), 'stripe_product_price_id', 'category')
=======
    fields = ('name', 'image', 'descriprtion', ('price', 'quantity'), 'category')
>>>>>>> de9e5cf (First commit)
    readonly_fields = ('descriprtion',)
    search_fields = ('name',)
    ordering = ('-name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    readonly_fields = ('created_timestamp',)
    extra = 0
