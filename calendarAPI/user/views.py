from typing import Any

from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from user.models import User
from user.serializers import UserRegistrationSerializer, UsersListSerializer


class UsersListView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = request.data
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST, content_type=serializer.errors)
        serializer.create(serializer.data)
        return Response(data=data, status=status.HTTP_201_CREATED)

