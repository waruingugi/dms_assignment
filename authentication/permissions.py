from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from commons.constants import UserRoles


class IsStaffPermission(BasePermission):
    """
    Custom permission to only allow staff API keys to make requests.
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        return request.user.is_authenticated and request.user.is_staff  # type: ignore


class IsSuperAdminOrSeniorDoctor(BasePermission):
    """
    Allows access only to super admin or senior doctor users.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the appropriate role
        return request.user.is_authenticated and (
            request.user.role == UserRoles.SENIOR_DOCTOR.value
            or request.user.is_superuser is True
        )
