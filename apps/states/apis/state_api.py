from typing import Any
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..serializers.state_serializer import StateSerializer
from ..services.state_service import StateService
from drf_yasg.utils import swagger_auto_schema

class StateViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.service = StateService()


    @swagger_auto_schema(request_body=StateSerializer)
    def create(self, request):
        serializer = StateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            state = self.service.create_state(
                name=serializer.validated_data['name'],
                value=serializer.validated_data['value'],
                is_initial=serializer.validated_data['is_initial'],
                is_final=serializer.validated_data['is_final']
            )

            return Response(state, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                { 'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk=None):
        state = self.service.delete_state(pk)

        if state:
            return Response(state, status=status.HTTP_200_OK)

        return Response(
            { 'error': 'State not found' },
            status=status.HTTP_404_NOT_FOUND
        )