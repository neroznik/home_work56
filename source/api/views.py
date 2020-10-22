from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import action
from rest_framework.permissions import  AllowAny, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from api.permissions import GETModelPermissions
from api.serializers import ProductSerializer, UserSerializer, OrderSerializer
from webapp.models import Product, Order


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class ProductViewSet(ViewSet):
    queryset = Product.objects.all()


    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [DjangoModelPermissions()]
        else:
            return [AllowAny()]

    def list(self, request):
        objects = Product.objects.all()
        slr = ProductSerializer(objects, many=True, context={'request': request})
        return Response(slr.data)

    def create(self, request):
        slr = ProductSerializer(data=request.data, context={'request': request})
        if slr.is_valid():
            slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        slr = ProductSerializer(product, context={'request': request})
        return Response(slr.data)

    def update(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        slr = ProductSerializer(data=request.data, instance=product, context={'request': request})
        if slr.is_valid():
            slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'pk': pk})


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class OrderViewSet(ViewSet):
    queryset = Order.objects.all()


    def get_permissions(self):
        if self.action in ['list', 'retrieve','create']:
            return [DjangoModelPermissions()]
        else:
            return [AllowAny()]

    def list(self, request):
        objects = Order.objects.all()
        slr = OrderSerializer(objects, many=True, context={'request': request})
        return Response(slr.data)

    def create(self, request):
        slr = OrderSerializer(data=request.data, context={'request': request})
        if slr.is_valid():
            slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def retrieve(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        slr = OrderSerializer(order, context={'request': request})
        return Response(slr.data)
