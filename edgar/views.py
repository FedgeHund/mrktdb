from edgar.models import Company,Filer,QuarterlyHolding,Security,QuarterlyOtherManager,QuarterlyOtherManagerDistribution,QuarterlySecurityHolding
from edgar.serializers import CompanySerializer,FilerSerializer,QuarterlyHoldingSerializer,SecuritySerializer,QuarterlyOtherManagerSerializer, QuarterlySecurityHoldingSerializer, QuarterlyOtherManagerDistributionSerializer
from rest_framework import generics


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class FilerList(generics.ListCreateAPIView):
    queryset = Filer.objects.all()
    serializer_class = FilerSerializer

class FilerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filer.objects.all()
    serializer_class = FilerSerializer

class QuarterlyHoldingList(generics.ListCreateAPIView):
    queryset = QuarterlyHolding.objects.all()
    serializer_class = QuarterlyHoldingSerializer

class QuarterlyHoldingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuarterlyHolding.objects.all()
    serializer_class = QuarterlyHoldingSerializer
    
class SecurityList(generics.ListCreateAPIView):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer


class SecurityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer

class QuarterlyOtherManagerList(generics.ListCreateAPIView):
    queryset = QuarterlyOtherManager.objects.all()
    serializer_class = QuarterlyOtherManagerSerializer


class QuarterlyOtherManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuarterlyOtherManager.objects.all()
    serializer_class = QuarterlyOtherManagerSerializer

class QuarterlyOtherManagerDistributionList(generics.ListCreateAPIView):
    queryset = QuarterlyOtherManagerDistribution.objects.all()
    serializer_class = QuarterlyOtherManagerDistributionSerializer


class QuarterlyOtherManagerDistributionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuarterlyOtherManagerDistribution.objects.all()
    serializer_class = QuarterlyOtherManagerDistributionSerializer

class QuarterlySecurityHoldingList(generics.ListCreateAPIView):
    queryset = QuarterlySecurityHolding.objects.all()
    serializer_class = QuarterlySecurityHoldingSerializer


class QuarterlySecurityHoldingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuarterlySecurityHolding.objects.all()
    serializer_class = QuarterlySecurityHoldingSerializer