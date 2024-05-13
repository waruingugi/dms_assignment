from typing import Any, Optional

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.base_model import Base
from commons.constants import UserRoles


class SimpleUserManager(BaseUserManager):
    def create_user(
        self,
        *,
        email: Optional[str],
        password: Optional[str] = None,
        **extra_fields: Any,
    ) -> "User":
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The given email must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)  # type: ignore
        user.save(using=self._db)
        return user  # type: ignore

    def create_superuser(
        self,
        *,
        email: Optional[str],
        password: Optional[str] = None,
        **extra_fields: Any,
    ) -> "User":
        """
        Create and save a superuser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(_("Superuser must have is_staff=True."))
        if not extra_fields.get("is_superuser"):
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, Base):
    """A custom user model"""

    first_name = models.CharField(_("First Name"), max_length=10, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=10, blank=True, null=True)
    email = models.EmailField(_("Email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(_("User is verified"), default=True)
    created_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_users",
    )
    role = models.CharField(
        max_length=20, choices=UserRoles.choices(), default=UserRoles.PATIENT
    )

    objects = SimpleUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []
