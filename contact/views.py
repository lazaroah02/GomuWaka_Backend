from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializer import ContactSerializer
# Create your views here.

class Contact(APIView):
    serializer_class = ContactSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            try:
                send_mail(
                serializer.validated_data['topic'],
                serializer.validated_data['message'],
                serializer.validated_data['email'],
                'lazaroah02@gmail.com'
                )
                return Response(['Email enviado correctamente'], status = status.HTTP_200_OK)
            except:
                return Response(['Error al enviar el email'],status = status.HTTP_404_NOT_FOUND)
        return Response(['Error al enviar el email'],status = status.HTTP_404_NOT_FOUND)
            
        
        