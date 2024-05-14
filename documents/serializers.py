from rest_framework import serializers

from dms.settings import MAX_FILE_SIZE_MB
from documents.models import Documents, DocumentType


class DocumentHistorySerializer(serializers.ModelSerializer):
    history_change_reason = serializers.CharField()
    history_user = serializers.CharField()
    history_date = serializers.CharField()
    deleted_by_id = serializers.CharField()
    history_id = serializers.CharField()
    file = serializers.CharField()

    class Meta:
        model = Documents
        fields = "__all__"
        read_only_fields = (
            "history_change_reason",
            "history_user",
            "history_date",
            "history_id",
            "deleted_by_id",
            "file",
        )


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = [
            "id",
            "created_at",
            "type",
            "created_by",
            "patient",
            "file",
            "id",
            "created_by",
            "notes",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "created_by": {"read_only": True},
            "notes": {"required": False},
        }

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


class DocumentVersionUpdateSerializer(serializers.Serializer):
    document_id = serializers.CharField()
    history_id = serializers.IntegerField()

    extra_kwargs = {"history_id": {"required": True}, "document_id": {"required": True}}
