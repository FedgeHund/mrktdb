from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import WatchlistSerializer
from .models import Watchlist


class WatchlistView(APIView):
    def get(self, request):
    	user = self.request.user
    	companies = Watchlist.objects.filter(user=user)
    	serializer = WatchlistSerializer(companies, many=True)
    	return Response({"watchlist": serializer.data})