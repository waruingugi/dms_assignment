from rest_framework import serializers

from dms.settings import MAX_FILE_SIZE_MB
from documents.models import Documents, DocumentType


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = [
            "id",
            "type",
            "created_by",
            "patient",
            "file",
            "id",
            "is_deleted",
            "created_by",
            "deleted_at",
        ]
        read_only_fields = ("created_by", "id", "is_deleted", "deleted_at")

    def validate_file(self, value):
        """Validate file is less than max size"""
        if value.size > MAX_FILE_SIZE_MB:
            raise serializers.ValidationError(
                f"File too large. Size should not exceed {MAX_FILE_SIZE_MB / (1024 * 1024)}."
            )
        return value


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ["id", "type", "created_by", "description"]
        read_only_fields = ["id", "created_by"]

    def validate_type(self, value):
        """Change type field to uppercase."""
        return value.upper()

    def create(self, validated_data):
        """Additionaly, set the 'created_by' to the current user"""
        request = self.context["request"]
        validated_data["created_by"] = request.user
        return super().create(validated_data)
