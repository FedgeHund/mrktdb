from .models import Position
from holdings.serializers import PositionSerializer, NumberOfFilersHoldingTheStockSerializer, TotalNumberOfSharesHeldSerializer, NetBuysSerializer, NetSellsSerializer
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count, Q, Sum

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

class LatestQuarterBiggestHoldings(generics.ListAPIView):
    serializer_class = PositionSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Position.objects.all()
            cik = self.request.GET.get('cik', None)
            if cik is not None:
                queryset = queryset.filter(cik=cik).order_by('-quarter', '-marketValue')
                latest_quarter = queryset[0].quarter
                queryset = queryset.filter(quarter=latest_quarter)[:5]
                
            return queryset

class LatestQuarterTopBuys(generics.ListAPIView):
    serializer_class = PositionSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Position.objects.all()
            cik = self.request.GET.get('cik', None)
            if cik is not None:
                queryset = queryset.filter(cik=cik).order_by('-quarter')
                latest_quarter = queryset[0].quarter
                queryset = queryset.filter(Q(positionType='New') | Q(positionType='Increased'))
                queryset = queryset.order_by('-changeOfValue')
                queryset = queryset.filter(quarter=latest_quarter)[:5]
                print(queryset.query)
                
            return queryset

class LatestQuarterTopSells(generics.ListAPIView):
    serializer_class = PositionSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Position.objects.all()
            cik = self.request.GET.get('cik', None)
            if cik is not None:
                queryset = queryset.filter(cik=cik).order_by('-quarter')
                latest_quarter = queryset[0].quarter
                queryset = queryset.filter(positionType='Decreased')
                queryset = queryset.order_by('-changeOfValue')
                queryset = queryset.filter(quarter=latest_quarter)[:5]
                print(queryset.query)
                
            return queryset

class AllOwnedSecurities(generics.ListAPIView):
    serializer_class = PositionSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Position.objects.values('cusip', 'securityName')
            cik = self.request.GET.get('cik', None)

            if cik is not None:
                queryset = queryset.filter(cik=cik)
                queryset = queryset.annotate(unique_cusips=Count('cusip', distinct=True))
                
            return queryset

class OwnershipHistory(generics.ListAPIView):
    serializer_class = PositionSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Position.objects.all()
            cik = self.request.GET.get('cik', None)
            cusip = self.request.GET.get('cusip', None)

            if cik is not None:
                queryset = queryset.filter(cik=cik, cusip=cusip)
                
            return queryset

# Single stock dashboard
class NumberOfFilersHoldingTheStock(generics.ListAPIView):
    serializer_class = NumberOfFilersHoldingTheStockSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Position.objects.all()
            ticker = self.request.GET.get('ticker', None)

            if ticker is not None:
                queryset = queryset.filter(ticker=ticker)
                queryset = queryset.values("quarter").annotate(numberHolding=Count("quarter", distinct=True))
                queryset = queryset.order_by("quarter")
                
            return queryset

class TotalNumberOfSharesHeld(generics.ListAPIView):
    serializer_class = TotalNumberOfSharesHeldSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Position.objects.all()
            ticker = self.request.GET.get('ticker', None)

            if ticker is not None:
                queryset = queryset.filter(ticker=ticker)
                queryset = queryset.values("quarter").annotate(totalSharesHeld=Sum("quantity", distinct=True))
                queryset = queryset.order_by("quarter")
                
            return queryset

class NetBuys(generics.ListAPIView):
    serializer_class = NetBuysSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Position.objects.all()
            ticker = self.request.GET.get('ticker', None)

            if ticker is not None:
                queryset = queryset.filter(ticker=ticker)
                queryset = queryset.filter(Q(positionType='New') | Q(positionType='Increased'))
                queryset = queryset.values("quarter").annotate(netBuys=Sum("changeInShares", distinct=True))
                queryset = queryset.order_by("quarter")
                
            return queryset

class NetSells(generics.ListAPIView):
    serializer_class = NetSellsSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Position.objects.all()
            ticker = self.request.GET.get('ticker', None)

            if ticker is not None:
                queryset = queryset.filter(ticker=ticker)
                queryset = queryset.filter(positionType='Decreased')
                queryset = queryset.values("quarter").annotate(netSells=Sum("changeInShares", distinct=True))
                queryset = queryset.order_by("quarter")
                
            return queryset