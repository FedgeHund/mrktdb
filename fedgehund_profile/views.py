from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import WatchlistSerializer
from .serializers import ProfileSerializer
from .models import Watchlist, Profile

class ProfileView(ListCreateAPIView):
	serializer_class = ProfileSerializer
	def get_queryset(self):
		return Profile.objects.filter(user=self.request.user)

	def post():
		Profile.objects.filter(user=self.request.user).update()


class WatchlistView(APIView):
    def get(self, request):
    	user = self.request.user
    	companies = Watchlist.objects.filter(user=user)
    	serializer = WatchlistSerializer(companies, many=True)
    	return Response({"watchlist": serializer.data})
