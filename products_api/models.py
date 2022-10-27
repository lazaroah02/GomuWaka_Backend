from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_es = models.CharField(max_length= 255)
    nombre_en = models.CharField(max_length= 255, default = ' ')
    nombre_turk = models.CharField(max_length= 255, default = ' ')
    img = models.ImageField(upload_to = "categories_images", default = "productos_images/blank.png")
    description_es = models.TextField(default = '',blank = True)
    description_en = models.TextField(default = '',blank = True)
    description_turk = models.TextField(default = '',blank = True)
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.nombre_es

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    product_img1 = models.ImageField(upload_to = "productos_images", default = "productos_images/blank.png")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ["id"]
    
