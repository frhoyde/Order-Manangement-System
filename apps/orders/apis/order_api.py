from typing import Any
from rest_framework import viewsets, status
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from ..serializers.order_serializer import CreateOrderSerializer
from ..services.order_service import OrderService

class OrderViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.service = OrderService()

    def create(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        try:
            order = self.service.create_order(
                items_data=serializer.validated_data['items']
            )

            return Response(order, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                { 'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        order = self.service.get_Order(pk)
        if order:
            return Response(order, status=status.HTTP_200_OK)
        return Response(
            { 'error': 'Order not found' },
            status=status.HTTP_404_NOT_FOUND
        )

    def update(self, request, pk=None):
        status_data = request.data.get('status')
        if not status_data:
            return Response(
                { 'error': 'Status is required' },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        order = self.service.update_order_status(pk, status_data, request.user.id)

        if order:
            return Response(order, status=status.HTTP_200_OK)

        return Response(
            { 'error': 'Order not found' },
            status=status.HTTP_404_NOT_FOUND
        )
    



