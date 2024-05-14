from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from authentication.permissions import IsStaffPermission, IsSuperAdminOrSeniorDoctor
from documents.models import Documents, DocumentType
from documents.serializers import (
    DocumentHistorySerializer,
    DocumentSerializer,
    DocumentTypeSerializer,
    DocumentVersionUpdateSerializer,
)


@extend_schema(tags=["Documents"])
class DocumentDownloadBaseView(APIView):
    """A lite version of the document base view"""

    permission_classes = [IsStaffPermission]


@extend_schema(tags=["Documents"])
class DocumentBaseView(GenericAPIView):
    """Base Document View"""

    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsStaffPermission]


@extend_schema(tags=["Document Types"])
class DocumentTypeBaseView(GenericAPIView):
    """Base Document Type View"""

    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [IsStaffPermission]


@extend_schema(tags=["Documents History"])
class DocumentHistoryBaseView(GenericAPIView):
    serializer_class = DocumentHistorySerializer
    queryset = Documents.history.all()
    permission_classes = [IsSuperAdminOrSeniorDoctor]


@extend_schema(tags=["Documents History"])
class DocumentBaseVersionUpdateView(APIView):
    """Revert document to a specific version."""

    serializer_class = DocumentVersionUpdateSerializer
    permission_classes = [IsSuperAdminOrSeniorDoctor]
