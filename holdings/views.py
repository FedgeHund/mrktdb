from .models import Position
from holdings.serializers import PositionSerializer
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 200

class PositionList(generics.ListAPIView):
    search_fields = ['^cik']
    filter_backends = (filters.SearchFilter,)
    queryset = Position.objects.all()
    pagination_class = StandardResultsSetPagination
    serializer_class = PositionSerializer

class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class LatestQuarterPositionList(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    serializer_class = PositionSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Position.objects.all()
            cik = self.request.GET.get('cik', None)
            if cik is not None:
                queryset = queryset.filter(cik=cik).order_by('-quarter')
                latest_quarter = queryset[0].quarter
                queryset = queryset.filter(quarter=latest_quarter)
                
            return queryset
