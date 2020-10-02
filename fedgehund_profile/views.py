from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import WatchlistSerializer
from .serializers import ProfileSerializer
from .models import Watchlist, Profile
from rest_framework import status

class ProfileView(ListCreateAPIView):
	serializer_class = ProfileSerializer
	def get_queryset(self):
		return Profile.objects.filter(user=self.request.user)

	def post(self, request):
		occupation = request.data['occupation']
		company = request.data['company']
		state = request.data['state']
		city = request.data['city']
		zip_code = request.data['zip_code']
		phone = request.data['phone']

		if occupation != "":
			Profile.objects.filter(user=self.request.user).update(occupation = occupation)
		if company != "":
			Profile.objects.filter(user=self.request.user).update(company = company)
		if state != "":
			Profile.objects.filter(user=self.request.user).update(state = state)
		if city != "":
			Profile.objects.filter(user=self.request.user).update(city = city)
		if zip_code != "":
			Profile.objects.filter(user=self.request.user).update(zip_code = zip_code)
		if phone != "":
			Profile.objects.filter(user=self.request.user).update(phone = phone)

		return Response(data = Profile.objects.filter(user=self.request.user).values())


class WatchlistView(APIView):
    def get(self, request):
    	user = self.request.user
    	companies = Watchlist.objects.filter(user=user)
    	serializer = WatchlistSerializer(companies, many=True)
    	return Response({"watchlist": serializer.data})