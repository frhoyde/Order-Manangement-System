from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from ..services.product_services import ProductService
from ..serializers.product_serializer import MutateProductSerializer
from drf_yasg.utils import swagger_auto_schema

class ProductViewSet(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ProductService()
    
    def list(self, request):
        products = self.service.get_all_products()
        return Response(products)
    
    def retrieve(self, request, pk=None):
        product = self.service.get_product(pk)
        if product:
            return Response(product)
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    @swagger_auto_schema(request_body=MutateProductSerializer)
    def create(self, request):
        try:
            product = self.service.create_product(request.data)
            return Response(product, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    @swagger_auto_schema(request_body=MutateProductSerializer)
    def update(self, request, pk=None):
        try:
            product = self.service.update_product(pk, request.data)
            if product:
                return Response(product)
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def destroy(self, request, pk=None):
        if self.service.delete_product(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )
