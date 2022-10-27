from django.contrib import admin
from django.urls import path,include
import products_api.urls
import contact.urls
import about.urls

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include(products_api.urls)),
    path('contact/', include(contact.urls)),
    path('about/', include(about.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
