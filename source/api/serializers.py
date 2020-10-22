from django.contrib.auth import get_user_model
from rest_framework import serializers

from webapp.models import Product, Order, OrderProduct


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


class OrdProSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    products = OrdProSerializer(many=True, read_only=True, source='product')

    class Meta:
        model = Order
        exclude =[]


