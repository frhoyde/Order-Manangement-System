from typing import List, Optional
from ..models.order import Order, OrderItem, OrderType
from apps.products.models.product import Product
class OrderRepository:
    def create_order(self, total_amount: float, order_type: OrderType) -> Order:
        try:
            order = Order.objects.create(
                total_amount=total_amount,
                status='1',  # Assuming 1 is the initial status
                order_type=order_type  # Use the object directly instead of order_type_id
            )
            return order
        except Exception as e:
            raise ValueError({"detail": f"Failed to create order: {str(e)}"})

    
    def create_order_item(self, order: Order, product_id: int, quantity: int) -> OrderItem:
        return OrderItem.objects.create(
            order=order,
            product_id=product_id,
            quantity=quantity,
        )
    
    def create_order_type(self, customer_type: str, service_type: str) -> OrderType:
        print(customer_type)
        return OrderType.objects.create(
            customer_type = customer_type,
            service_type = service_type
        )

    def get_all_orders(self) -> List[Order]:
        return Order.objects.all()

    def get_all_order_types(self) -> List[OrderType]:
        return OrderType.objects.all()

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        return Order.objects.filter(id=order_id).first()

    def get_order_type_by_id(self, order_type_id: int) -> Optional[OrderType]:
        return OrderType.objects.filter(id=order_type_id).first()

    def update_order_status(self, order: Order) -> Optional[Order]:
        if order:
            order.save()
        return order


    