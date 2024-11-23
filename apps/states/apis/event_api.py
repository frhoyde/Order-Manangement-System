from typing import Any
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..serializers.event_serializer import EventSerializer
from ..services.state_service import StateService
from ..services.event_service import EventService
from drf_yasg.utils import swagger_auto_schema


class EventViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.state_service = StateService()
        self.event_service = EventService()
        
    
    @swagger_auto_schema(request_body=EventSerializer)
    def create(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            event = self.event_service.create_event(
                name=serializer.validated_data['name'],
                sources=serializer.validated_data['sources'],
                destinations=serializer.validated_data['destination'],
                order_type_id=serializer.validated_data['order_type_id']
            )

            return Response(event, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                { 'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )