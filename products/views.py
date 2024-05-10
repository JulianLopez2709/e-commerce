from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer
from core.paguination import CustomPagination

@api_view(['GET'])
def get_products(req):
    products= Product.objects.all()
    pagination= CustomPagination()
    paginated_products = pagination.paginate_queryset(products, req)
    serializer = ProductSerializer(paginated_products,many= True)
    return pagination.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_product(req,name):
    products= Product.objects.get(name=name)
    serializer = ProductSerializer(products,many= False)
    return Response( serializer.data)


@api_view(['POST'])
def create_product(request):
    print(request.user)
    if request.user.is_staff:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['PUT'])
def edit_product(req, pk):
    product = Product.objects.get(pk = pk)
    if req.user.is_staff:
        serializer = ProductSerializer(product,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response( serializer.data, status=status.HTTP_400_BAD_REQUEST) 
    else:
        return Response( serializer.data, status=status.HTTP_401_UNAUTHORIZED)       


@api_view(['DELETE'])
def delete_product(req, pk):
    product = Product.objects.get(pk = pk)
    if req.user.is_staff:
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)       
