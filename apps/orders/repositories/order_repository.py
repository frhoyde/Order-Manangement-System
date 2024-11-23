from typing import List, Optional
from ..models.order import Order, OrderItem, OrderType
from apps.products.models.product import Product
class OrderRepository:
    def create_order(self, total_amount: float) -> Order:
        order = Order.objects.create(
            total_amount = total_amount,
            status = 1
        )
        print(f"State {order.sm.current_state.name}")
        return order
    
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

    def update_order_status(self, order_id: int) -> Optional[Order]:
        order = self.get_order_by_id(order_id)
        order.sm.flow()
        if order:
            order.save()
        return order


    