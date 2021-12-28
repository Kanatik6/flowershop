from django.contrib import admin
from apps.products.models import Product, ProductItem

class ProductInline(admin.StackedInline):
    model = ProductItem
    extra = 1
    # formset = Product.objects.all()

class ProductItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category",'price','size','is_new','discount',)
    search_fields = ('title','category')
    list_filter = ('price','title','quantity','discount','category')
    # inlines = [
    #     ProductInline
    # ]
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductInline,]

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductItem,ProductItemAdmin)
