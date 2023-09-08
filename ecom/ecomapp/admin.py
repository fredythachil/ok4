from django.contrib import admin
from .models import Categories,Product

# Register your models here.
class adminCategories(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(Categories,adminCategories)
class adminProduct(admin.ModelAdmin):
    list_display = ['name','stock','availability','price','slug','categories']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 5
    list_editable = ['stock','availability','price','categories']
admin.site.register(Product,adminProduct)