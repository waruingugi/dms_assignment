from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
)

from authentication.models import User
from authentication.permissions import IsStaffPermission, IsSuperAdminOrSeniorDoctor
from authentication.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Create a user"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsStaffPermission]

    def get_serializer_context(self) -> dict:
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class UserListAPIView(ListAPIView):
    """List Users"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsStaffPermission]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["first_name", "last_name", "email"]
    filterset_fields = ["is_verified", "is_staff"]
    ordering_fields = ["created_at"]


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """Retrieve a user"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsStaffPermission]
    lookup_field = "id"


class UserDeleteAPIView(DestroyAPIView):
    """Delete a user"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperAdminOrSeniorDoctor]
    lookup_field = "id"
