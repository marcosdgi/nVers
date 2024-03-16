from rest_framework.serializers import ModelSerializer

from Services.models.Service import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
