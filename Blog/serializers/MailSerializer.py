from rest_framework.serializers import ModelSerializer

from Blog.models.Mail import Mail


class MailSerializer(ModelSerializer):
    class Meta:
        model = Mail
        fields = '__all__'
