from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.store.models import Product, ProductCategories
from apps.store.serializer import ProductSerializer, ProductCategorySerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductsAPIView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['price', 'is_active']
    serializer_class = ProductSerializer
    search_fields = ['title']
    ordering_fields = ['price', 'created_at']
    queryset = Product.objects.all()
    print(queryset)

    def post(self, request):
        request_body = request.data
        new_product = Product.objects.create(title=request_body['title'],
                                             description=request_body['description'],
                                             price=request_body['price'],
                                             is_active=request_body['is_active'])
        srz = ProductSerializer(new_product, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class ProductRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = ProductSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return JsonResponse({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class ProductCategoriesAPIView(generics.ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategories.objects.all()

    def post(self, request):
        request_body = request.data
        new_product = ProductCategories.objects.create(title=request_body['title'],
                                                       )
        srz = ProductCategorySerializer(new_product, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class CategoryRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            category = ProductCategories.objects.get(id=pk)
        except ProductCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = ProductCategorySerializer(category, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            category = Product.objects.get(id=pk)
        except ProductCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        request_body = request.data
        new_product = User.objects.create(username=request_body['username'],
                                          password=request_body['password'],
                                          email=request_body['email']
                                          )
        srz = UserSerializer(new_product, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class UserRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({'msg': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = UserSerializer(user, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({'msg': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
