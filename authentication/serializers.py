from rest_framework import serializers

from authentication.models import User
from commons.constants import UserRoles


class UserSerializer(serializers.ModelSerializer):
    """User fields required when making a request"""

    first_name = serializers.CharField(max_length=10, required=True)
    last_name = serializers.CharField(max_length=10, required=False, allow_blank=True)
    role = serializers.ChoiceField(choices=UserRoles.choices(), required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "role", "created_by"]
        extra_kwargs = {"email": {"required": True}, "created_by": {"required": True}}

    def create(self, validated_data):
        """Create the user instance and automatically add them permissions of their
        assigned group.
        """
        request = self.context["request"]
        validated_data["created_by"] = request.user

        # Check the role and set 'is_staff' accordingly
        if validated_data["role"] != UserRoles.PATIENT.value:
            validated_data["is_staff"] = True

        return super().create(validated_data)
