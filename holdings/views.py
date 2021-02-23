from filer.models import QuarterlyFilerView
from .serializers import QuarterlyFilerViewSerializer
from rest_framework import generics


class QuarterlyFilerViewList(generics.ListCreateAPIView):
    queryset = QuarterlyFilerView.objects.all()
    serializer_class = QuarterlyFilerViewSerializer

class QuarterlyFilerViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuarterlyFilerView.objects.all()
    serializer_class = QuarterlyFilerViewSerializer