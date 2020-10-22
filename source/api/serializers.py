from django.contrib.auth import get_user_model
from rest_framework import serializers

from webapp.models import Product, Order


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True,
                                               view_name='api_v1:user-detail')

    class Meta:
        model = get_user_model()
        fields = ['id', 'url', 'username', 'first_name', 'last_name', 'email']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = []


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['phone','address', 'products']
        read_only_field = ['name']


