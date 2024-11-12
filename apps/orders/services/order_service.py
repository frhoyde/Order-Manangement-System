from typing import List, Optional
from django.db import transaction
from ..repositories.order_repository import OrderRepository
from ..serializers.order_serializer import OrderSerializer
from apps.products.repositories.product_repository import ProductRepository


class OrderService:
    def __init__(self):
        self.order_repository = OrderRepository()
        self.product_repository = ProductRepository()

    def create_order(self, items_data: List[dict]) -> dict:
            """Create a new order with items."""
            with transaction.atomic():
                total_amount = float(0.0)
                validated_items = []
                
                for item in items_data:
                    product = self.product_repository.get_by_id(item['product_id'])
                    if not product:
                        raise Exception(f"Product {item['product_id']} not found")
                    
                    item_total = product.price * item['quantity']
                    total_amount += item_total
                    validated_items.append({
                        'product': product,
                        'quantity': item['quantity'],
                        'price': product.price
                    })
                
                # Create order
                order = self.order_repository.create_order(
                total_amount=total_amount
            )
            
            # Create order items
            for item in validated_items:
                self.order_repository.create_order_item(
                    order=order,
                    product_id=item['product'].id,
                    quantity=item['quantity'],
                )
            
            return OrderSerializer(order).data
    
    def get_all_orders(self) -> List[dict]:
        orders = self.order_repository.get_all_orders()
        return OrderSerializer(orders, many=True).data

    def get_Order(self, order_id: int) -> Optional[dict]:
        order = self.order_repository.get_order_by_id(order_id)
        return OrderSerializer(order).data if order else None
    
    def update_order_status(self, order_id: int, status: str) -> Optional[dict]:
        order = self.order_repository.get_order_by_id(order_id)

        if not order:
            return None

        updated_order = self.order_repository.update_order_status(order_id, status)

        return OrderSerializer(updated_order).data if updated_order else None