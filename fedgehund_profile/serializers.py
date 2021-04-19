from .models import Profile, Watchlist
from rest_framework import serializers
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'occupation',
            'company',
            'city',
            'state',
            'phone',
            'zip_code']


class WatchlistSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='companies_watchlist.name')
    company_id = serializers.ReadOnlyField(
        source='companies_watchlist.companyId')
    security_name = serializers.ReadOnlyField(
        source='stock_watchlist.securityName')
    security_id = serializers.ReadOnlyField(
        source='stock_watchlist.securityId')

    class Meta:
        model = Watchlist
        fields = ['company_id', 'company_name', 'security_id', 'security_name']
