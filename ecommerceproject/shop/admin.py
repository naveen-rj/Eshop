from django.contrib import admin

from shop.models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # to customize admin panel columns
    list_display = ['name', 'slug']
    # when typing name field, slug field will automatically fill
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
