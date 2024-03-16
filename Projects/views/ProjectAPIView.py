from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Projects.models.Projects import Project
from Projects.serializers.ProjectSerializer import ProjectSerializer


class ProjectAPIView(APIView):

    def get(self, request, format=None):
        try:
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is not None:
            project = Project.objects.get(id=pk)
            serializer = ProjectSerializer(project)
            if serializer.is_valid():
                data = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            project = Project.objects.get(id=pk)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)