from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Profile


class ProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        # user = get_object_or_404(User, pk=kwargs['user_id'])
        # profile_serializer = UserSerializer(user.profile)
        # return Response(profile_serializer.data)
        serializer = UserSerializer(request.user)
        return Response(serializer.data)