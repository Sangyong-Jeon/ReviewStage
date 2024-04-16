from rest_framework import viewsets

from performance_api.serializers import *


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
