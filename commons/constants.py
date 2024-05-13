from enum import Enum


class UserRoles(str, Enum):
    """User Roles"""

    PATIENT = "PATIENT"
    DOCTOR = "DOCTOR"
    SENIOR_DOCTOR = "SENIOR_DOCTOR"

    @classmethod
    def list_(cls) -> list:
        """Returns a list of the user roles"""
        roles = {role.value for role in cls}
        return list(roles)

    @classmethod
    def choices(cls):
        """Returns a list of tuples suitable for the choices in a Django model field"""
        return [(role.value, role.name.replace("_", " ").title()) for role in cls]
