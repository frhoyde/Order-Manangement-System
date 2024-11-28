from typing import List, Optional
from django.db import transaction
from django.forms import ValidationError
from ..repositories.order_repository import OrderRepository
from ..serializers.order_serializer import OrderSerializer, OrderTypeSerializer
from apps.products.repositories.product_repository import ProductRepository
from apps.states.services.event_service import EventService
from apps.states.services.state_service import StateService
from apps.states.state_machine import StateMachineService
from apps.core.state_adapter import StateAdapter
from threading import Event as ThreadingEvent
from threading import Thread


class OrderService:
    def __init__(self):
        self.order_repository = OrderRepository()
        self.product_repository = ProductRepository()
        self.event_service = EventService()
        self.state_service = StateService()
        self.state_machine_service = StateMachineService()

    def create_order(self, order_type_id: int, items_data: dict) -> dict:
        with transaction.atomic():
            # First validate order type exists
            order_type = self.order_repository.get_order_type_by_id(order_type_id)
            if not order_type:
                raise ValueError(f"OrderType with id {order_type_id} not found")

            # Calculate totals and validate products
            total_amount = 0.0
            validated_items = []
            
            if not items_data:
                raise ValueError("No items provided for order")

            for item in items_data:
                if not isinstance(item, dict):
                    raise ValueError(f"Invalid item format: {item}")
                    
                product_id = item.get('product_id')
                quantity = item.get('quantity')
                
                if not product_id or not quantity:
                    raise ValueError(f"Missing product_id or quantity in item: {item}")

                product = self.product_repository.get_by_id(product_id)
                if not product:
                    raise ValueError(f"Product {product_id} not found")

                item_total = float(product.price * quantity)
                total_amount += item_total
                
                validated_items.append({
                    'product': product,
                    'quantity': quantity,
                })

            # Create the order
            try:
                order = self.order_repository.create_order(
                    total_amount=total_amount,
                    order_type=order_type
                )

                # Create order items
                for item in validated_items:
                    self.order_repository.create_order_item(
                        order=order,
                        product_id=item['product'].id,
                        quantity=item['quantity'],
                    )

                # Refresh the order to get all related data
                order.refresh_from_db()
                return OrderSerializer(order).data

            except Exception as e:
                # Since we're in a transaction, this will roll back automatically
                raise ValidationError({"detail": f"Failed to create order: {str(e)}"})
    
    def get_all_orders(self) -> List[dict]:
        orders = self.order_repository.get_all_orders()
        return OrderSerializer(orders, many=True).data

    def get_Order(self, order_id: int) -> Optional[dict]:
        order = self.order_repository.get_order_by_id(order_id)
        return OrderSerializer(order).data if order else None
    
    def update_order_status(self, order_id: int, event_id: int) -> Optional[dict]:
        order = self.order_repository.get_order_by_id(order_id)

        if not order:
            return None

        event = self.event_service.get_event(event_id)

        if not event:
            raise Exception(f"Event {event_id} not found")
        
        
        # print(isinstance(order.sm, StateMachineService))
        order.sm.flow()

        updated_order = self.order_repository.update_order_status(order)

        return OrderSerializer(updated_order).data if updated_order else None