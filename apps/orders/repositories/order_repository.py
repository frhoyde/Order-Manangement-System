from typing import List, Optional
from ..models.order import Order, OrderItem
from apps.products.models.product import Product

class OrderRepository:
    def create_order(self, total_amount: float) -> Order:
        return Order.objects.create(
            total_amount = total_amount
        )
    
    def create_order_item(self, order: Order, product_id: int, quantity: int) -> OrderItem:
        return OrderItem.objects.create(
            order=order,
            product_id=product_id,
            quantity=quantity,
        )

    def get_all_orders(self) -> List[Order]:
        return Order.objects.all()

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        return Order.objects.filter(id=order_id).first()

    def update_order_status(self, order_id: int, status: str) -> Optional[Order]:
        order = self.get_order_by_id(order_id)
        if order:
            order.status = status
            order.save()
        return order


    