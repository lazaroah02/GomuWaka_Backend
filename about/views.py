from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import About

# Create your views here.
class About_api(APIView):
    def get(self, request, idioma = 'es'):
        if idioma == 'es':
            info = [{
                'id':inf.id,
                'about':inf.about_es,
                'email_contact':inf.email_contact,
                'telefono':inf.telefono,
                'certificado':inf.certificado.url,
                'img':inf.img.url,
            } for inf in About.objects.all()]
            return Response(info,status = status.HTTP_200_OK)
        
        elif idioma == 'en':
            info = [{
                'id':inf.id,
                'about':inf.about_en,
                'email_contact':inf.email_contact,
                'telefono':inf.telefono,
                'certificado':inf.certificado.url,
                'img':inf.img.url,
            } for inf in About.objects.all()]
            return Response(info,status = status.HTTP_200_OK)
        elif idioma == 'turk':
            info = [{
                'id':inf.id,
                'about':inf.about_turk,
                'email_contact':inf.email_contact,
                'telefono':inf.telefono,
                'certificado':inf.certificado.url,
                'img':inf.img.url,
            } for inf in About.objects.all()]
            return Response(info,status = status.HTTP_200_OK)

class Email_api(APIView):
    def get(self, request):
        info = [{'email':inf.email_contact} for inf in About.objects.all()]
        return Response(info,status = status.HTTP_200_OK)
           