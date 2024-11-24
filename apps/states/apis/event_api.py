from typing import Any
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..serializers.event_serializer import EventSerializer, EventCreateSerializer
from ..services.state_service import StateService
from ..services.event_service import EventService
from drf_yasg.utils import swagger_auto_schema


class EventViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.state_service = StateService()
        self.event_service = EventService()
        
    
    @swagger_auto_schema(request_body=EventCreateSerializer)
    def create(self, request):
        serializer = EventCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            event = self.event_service.create_event(dict(
                name=serializer.validated_data['name'],
                sources=serializer.validated_data['sources'],
                destinations=serializer.validated_data['destinations'],
                orderType=serializer.validated_data['orderType']
            ))

            return Response(event, status=status.HTTP_201_CREATED)
        except Exception as e:
            raise e
    
    def retrieve(self, request, pk):
        try:
            events = self.event_service.get_available_events(pk)
            return Response(events, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                { 'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
