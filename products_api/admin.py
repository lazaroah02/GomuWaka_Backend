from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_es","img")

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "product_img1", "updated_at")
    list_filter = ("categoria",)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)

