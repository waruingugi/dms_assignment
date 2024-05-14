import requests
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from authentication.permissions import IsSuperAdminOrSeniorDoctor
from documents.base_views import (
    DocumentBaseVersionUpdateView,
    DocumentBaseView,
    DocumentDownloadBaseView,
    DocumentHistoryBaseView,
    DocumentTypeBaseView,
)
from documents.models import Documents


class DocumentUploadView(DocumentBaseView, CreateAPIView):
    """Handle file uploads"""

    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DocumentListAPIView(DocumentBaseView, ListAPIView):
    """List documents"""

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        "patient__first_name",
        "patient__last_name",
        "patient__email",
        "notes",
    ]
    filterset_fields = ["is_deleted"]
    ordering_fields = ["created_at"]


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

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["type", "description"]
    ordering_fields = ["created_at"]


class DocumentTypeRetrieveUpdateAPIView(DocumentTypeBaseView, RetrieveUpdateAPIView):
    """Retrieve a document type"""

    lookup_field = "id"


class DocumentTypeDeleteAPIView(DocumentTypeBaseView, DestroyAPIView):
    """Delete a document type"""

    permission_classes = [IsSuperAdminOrSeniorDoctor]
    lookup_field = "id"


class DocumentsHistoryListView(DocumentHistoryBaseView, ListAPIView):
    """List all document history"""

    pass


class DocumentHistoryDetailView(DocumentHistoryBaseView, ListAPIView):
    """Detailed document version"""

    lookup_field = "id"

    def get_queryset(self):
        document = get_object_or_404(Documents, id=self.kwargs.get("id"))
        return document.history.all()


class DocumentVersionUpdateView(DocumentBaseVersionUpdateView):
    def post(self, request, *args, **kwargs):
        """Revert document to a specific version."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            document_id = serializer.validated_data["document_id"]
            history_id = serializer.validated_data["history_id"]

            try:
                document = Documents.objects.get(id=document_id)
                historical_record = document.history.get(history_id=history_id)

                # Create a new instance from historical record
                new_document = Documents(
                    type=historical_record.type,
                    created_by=historical_record.created_by,
                    patient=historical_record.patient,
                    notes=historical_record.notes,
                    file=historical_record.file,  # Make sure to handle file fields appropriately
                    is_deleted=historical_record.is_deleted,
                    deleted_at=historical_record.deleted_at,
                    deleted_by=historical_record.deleted_by,
                )
                new_document.save()

            except Documents.DoesNotExist:
                return Response(
                    {"message": "Document not found."}, status=status.HTTP_404_NOT_FOUND
                )
            except ValidationError:
                return Response(
                    {"message": "UUID record not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            return Response(
                {"message": "Document version updated successfully."},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentDownloadView(DocumentDownloadBaseView):
    def get(self, request, *args, **kwargs):
        """Download a file"""
        document = get_object_or_404(Documents, id=self.kwargs.get("id"))

        response = requests.get(document.file.url, stream=True)
        if response.status_code != 200:
            return Response(
                {"message": "Failed to fetch file."}, status=response.status_code
            )

        # Create a HTTP response with the stream and correct content type
        file_response = HttpResponse(
            response.content, content_type=response.headers["Content-Type"]
        )
        file_response["Content-Disposition"] = (
            'attachment; filename="%s"' % document.file.name
        )
        return file_response
