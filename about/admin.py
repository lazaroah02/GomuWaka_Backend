from django.contrib import admin
from .models import About

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id","certificado")
    
admin.site.register(About, AboutAdmin)