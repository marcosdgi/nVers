from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Services.models.Service import Service
from Services.serializers.ServiceSerializer import ServiceSerializer


class ServiceAPIView(APIView):
    def get(self, request):
        try:
            services = Service.objects.all()
            services_serializer = ServiceSerializer(services, many=True)
            return Response(services_serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response({'data': data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is not None:
            services = Service.objects.get(id=pk)
            serializer = ServiceSerializer(instance=services, data=request.data)
            if serializer.is_valid():
                data = serializer.save()
                return Response({'data': data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            service = Service.objects.get(id=pk)
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
