from typing import List, Optional
from ..models.order import Order, OrderItem

class OrderRepository:
    def create_order(self, total_amount: float) -> Order:
        return Order.objects.create(
            total_amount = total_amount
        )
    
    def create_order_item(self, order: Order, product: str, quantity: int, price: float) -> OrderItem:
        return Order.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price
        )

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        return Order.objects.filter(id=order_id).first()

    def update_order_status(self, order_id: int, status: str) -> Optional[Order]:
        order = self.get_order_by_id(order_id)
        if order:
            order.status = status
            order.save()
        return order


    