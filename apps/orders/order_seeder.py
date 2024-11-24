from apps.orders.repositories.order_repository import OrderRepository
from apps.orders.constants.order_types import OrderTypeConstants
class OrderSeeder:
    def __init__(self) -> None:
        self.order_repository = OrderRepository()
        self.constants = OrderTypeConstants()

        existing_order_types = self.order_repository.get_all_order_types()

        if len(existing_order_types) == 0:
            print('Seeding Order Types')
            for customer_type in self.constants.customer_types:
                for service_type in self.constants.service_types:
                    order_type = self.order_repository.create_order_type(customer_type, service_type)
                    print(f'Customer Type: {order_type.customer_type}, Service Type: {order_type.service_type}')

        else:
            print(f'Order Types already Exist! Count: {len(existing_order_types)}')
            for order_type in existing_order_types:
                print(f'{order_type.id} - {order_type.customer_type} - {order_type.service_type}')
