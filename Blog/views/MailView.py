from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Blog.models.Mail import Mail
from Blog.serializers.MailSerializer import MailSerializer


class ReceiveEmailView(APIView):
    def get(self, request, format=None):
        try:
            mails = Mail.objects.all()
            serializer = MailSerializer(mails, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        sender_email = request.data.get('sender_email')
        reponse = {'message': 'Correo electrónico recibido correctamente'}
        return Response(reponse, status=status.HTTP_200_OK)
