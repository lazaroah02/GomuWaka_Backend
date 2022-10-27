from django.db import models

# Create your models here.
class About(models.Model):
    about_es = models.TextField(blank=True, default = ' ')
    about_en = models.TextField(blank=True, default = ' ')
    about_turk = models.TextField(blank=True, default = ' ')
    email_contact = models.EmailField(blank=True, null = True, default ='')
    telefono = models.CharField(max_length = 15, blank = True, null = True, default = '')
    certificado = models.ImageField(blank=True, null = True, upload_to = "info_company", default = "productos_images/blank.png")
    img = models.ImageField(blank=True, null = True, upload_to = "info_company", default = "productos_images/blank.png")
    
    def __str__(self):
        return self.about_es