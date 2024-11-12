from typing import List, Optional
from ..models.product import Product

class ProductRepository:
    def get_all(self) -> List[Product]:
        return Product.objects.all()
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None
    
    def create(self, product_data: dict) -> Product:
        return Product.objects.create(**product_data)
    
    def update(self, product_id: int, product_data: dict) -> Optional[Product]:
        product = self.get_by_id(product_id)
        if product:
            for key, value in product_data.items():
                setattr(product, key, value)
            product.save()
            return product
        return None
    
    def delete(self, product_id: int) -> bool:
        product = self.get_by_id(product_id)
        if product:
            product.delete()
            return True
        return False