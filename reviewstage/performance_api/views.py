from rest_framework.decorators import api_view
from rest_framework.response import Response

from performance.models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterUser(generics.CreateAPIView):
    serializer_class = RegisterSerializer


@api_view(['GET'])
def get_visual_file(request):
    if request.method == 'GET':
        performance_id = request.GET.get('performance_id')
        try:

            visual_file = File.objects.get(performance_id=performance_id, type=FileType.VISUAL.name)
            serializer = FileSerializer(visual_file)
            return Response(serializer.data)
        except File.DoesNotExist:
            return Response({'error': 'Visual file not found for the given performance ID'}, status=404)
