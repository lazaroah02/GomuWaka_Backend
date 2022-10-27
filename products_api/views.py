from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from django.core.paginator import Paginator
from .models import Producto, Categoria

# Create your views here.
class GetCategories(APIView):
    def get(self, request, idioma = 'es'):
        if idioma == 'es':
            categories = [{
                "id":category.id,
                "name":category.nombre_es,
                "img":category.img.url,
                'description':category.description_es}
                for category in Categoria.objects.all()]
            return Response(categories, status=status.HTTP_200_OK)
        if idioma == 'en':
            categories = [{
                "id":category.id,
                "name":category.nombre_en,
                "img":category.img.url,
                'description':category.description_en}
                for category in Categoria.objects.all()]
            return Response(categories, status=status.HTTP_200_OK)
        if idioma == 'turk':
            categories = [{
                "id":category.id,
                "name":category.nombre_turk,
                "img":category.img.url,
                'description':category.description_turk}
                for category in Categoria.objects.all()]
            return Response(categories, status=status.HTTP_200_OK)

class Get_Products_Of_Category(APIView):
    def get(self, request, category = None, idioma = 'es') :
        print('Hola')
        if category == None:
            return Response([],status = status.HTTP_404_NOT_FOUND)
        
        #get the category description filtering by the lenguage
        description_category = Categoria.objects.get(id = category)
        if idioma == 'es':
            description = description_category.description_es
        elif idioma == 'en':
            description = description_category.description_en
        elif idioma == 'turk':
            description = description_category.description_turk   
            
                 
        products = [{
            "id":product.id,
            "img":product.product_img1.url,
            }for product in Producto.objects.filter(categoria = category)] 
        if products == []:
            return Response([],status = status.HTTP_404_NOT_FOUND)
        return Response({"description":description,"products": products}, status = status.HTTP_200_OK)

   