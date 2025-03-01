from .models import Product
from .serializers import ProductSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductList(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(product, many = True)
        # print(serializer.data) dictionary
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # data = request.data
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetails(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id = id)
        except Product.DoesNotExist:
            msg = {'msg': 'Record Not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializers(product)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            product = Product.objects.get(id = id)
        except Product.DoesNotExist:
            msg = {'msg': 'Record Not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializers(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        product = Product.objects.get(id = id)

        serializer = ProductSerializers(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status= status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        product = Product.objects.get(id = id)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    



