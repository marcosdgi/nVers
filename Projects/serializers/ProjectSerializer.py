from rest_framework.serializers import ModelSerializer

from Projects.models.Projects import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
