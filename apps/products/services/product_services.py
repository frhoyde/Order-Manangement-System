from typing import List, Optional
from ..repositories.product_repository import ProductRepository
from ..serializers.product_serializer import ProductSerializer

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()
    
    def get_all_products(self) -> List[dict]:
        products = self.repository.get_all()
        serializer = ProductSerializer(products, many=True)
        return serializer.data
    
    def get_product(self, product_id: int) -> Optional[dict]:
        product = self.repository.get_by_id(product_id)
        if product:
            serializer = ProductSerializer(product)
            return serializer.data
        return None
    
    def create_product(self, product_data: dict) -> dict:
        serializer = ProductSerializer(data=product_data)
        if serializer.is_valid(raise_exception=True):
            product = self.repository.create(serializer.validated_data)
            return ProductSerializer(product).data
    
    def update_product(self, product_id: int, product_data: dict) -> Optional[dict]:
        product = self.repository.get_by_id(product_id)
        if product:
            serializer = ProductSerializer(product, data=product_data, partial=True)
            if serializer.is_valid(raise_exception=True):
                updated_product = self.repository.update(product_id, serializer.validated_data)
                return ProductSerializer(updated_product).data
        return None
    
    def delete_product(self, product_id: int) -> bool:
        return self.repository.delete(product_id)
