from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.parsers import FormParser, MultiPartParser

from authentication.permissions import IsSuperAdminOrSeniorDoctor
from documents.base_views import DocumentBaseView, DocumentTypeBaseView


class DocumentUploadView(DocumentBaseView, CreateAPIView):
    """Handle file uploads"""

    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DocumentListAPIView(DocumentBaseView, ListAPIView):
    """List documents"""

    pass


class DocumentRetrieveUpdateAPIView(DocumentBaseView, RetrieveUpdateAPIView):
    """Retrieve a document"""

    lookup_field = "id"


class DocumentDeleteAPIView(DocumentBaseView, DestroyAPIView):
    """Delete a document"""

    permission_classes = [IsSuperAdminOrSeniorDoctor]
    lookup_field = "id"


class DocumentTypeCreateView(DocumentTypeBaseView, CreateAPIView):
    """Create a document type."""

    def get_serializer_context(self) -> dict:
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class DocumentTypeListAPIView(DocumentTypeBaseView, ListAPIView):
    """List documents types"""

    pass


class DocumentTypeRetrieveUpdateAPIView(DocumentTypeBaseView, RetrieveUpdateAPIView):
    """Retrieve a document type"""

    lookup_field = "id"


class DocumentTypeDeleteAPIView(DocumentTypeBaseView, DestroyAPIView):
    """Delete a document type"""

    permission_classes = [IsSuperAdminOrSeniorDoctor]
    lookup_field = "id"
