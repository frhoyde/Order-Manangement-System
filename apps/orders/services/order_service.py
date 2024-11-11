from decimal import Decimal
from typing import List, Optional
from django.db import transaction
from ..repositories.order_repository import OrderRepository
from ..serializers.order_serializer import OrderSerializer


class OrderService:
    def __init__(self):
        self.order_repository = OrderRepository()

    def create_order(self, items_data: List[dict]) -> dict: 
        with transaction.atomic():
            total_amount = Decimal('0')
            validated_items = []

            for item in items_data:
                if len(item) < 0:
                    print("Error!")
                
                item_total = item['price'] * item['quantity']
                total_amount = item_total

                validated_items.append({
                    'product': item['product'],
                    'quantity': item['quantity'],
                    'price': item['price']
                })

            order = self.order_repository.create_order(
                total_amount=total_amount
            )

            for item in validated_items:
                self.order_repository.create_order_item(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )

            return OrderSerializer(order).data
    
    def get_Order(self, order_id: int) -> Optional[dict]:
        order = self.order_repository.get_order_by_id(order_id)

        return OrderSerializer(order.data) if order else None
    
    def update_order_status(self, order_id: int, status: str) -> Optional[dict]:
        order = self.order_repository.get_order_by_id

        if not order:
            return None

        updated_order = self.order_repository.update_order_status(order_id, status)

        return OrderSerializer(updated_order).data if updated_order else None