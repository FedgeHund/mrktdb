from filer.models import QuarterlyFilerView
from .serializers import QuarterlyFilerViewSerializer
from rest_framework import generics, filters


class LatestQuarterData13FSummaryTable(generics.ListAPIView):
    serializer_class = QuarterlyFilerViewSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = QuarterlyFilerView.objects.all()
            cik = self.request.GET.get('cik', None)
            if cik is not None:
                queryset = queryset.filter(cik=cik).order_by('-quarter')
                latest_quarter = queryset[0].quarter
                queryset = queryset.filter(quarter=latest_quarter)[:1]
                print(queryset.query)

            return queryset


class QuarterlyMarketValueChart(generics.ListAPIView):
    serializer_class = QuarterlyFilerViewSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = QuarterlyFilerView.objects.all()
            cik = self.request.GET.get('cik', None)
            if cik is not None:
                queryset = queryset.filter(cik=cik).order_by('quarter')

            return queryset


class QuarterlyFilerViewList(generics.ListCreateAPIView):
    search_fields = ['^cik']
    filter_backends = (filters.SearchFilter,)
    queryset = QuarterlyFilerView.objects.all()
    serializer_class = QuarterlyFilerViewSerializer


class QuarterlyFilerViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuarterlyFilerView.objects.all()
    serializer_class = QuarterlyFilerViewSerializer
