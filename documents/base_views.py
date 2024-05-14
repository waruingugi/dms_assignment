from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView

from authentication.permissions import IsStaffPermission
from documents.models import Documents, DocumentType
from documents.serializers import DocumentSerializer, DocumentTypeSerializer


@extend_schema(tags=["Documents"])
class DocumentBaseView(GenericAPIView):
    """Base Document View"""

    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsStaffPermission]


@extend_schema(tags=["Document-Types"])
class DocumentTypeBaseView(GenericAPIView):
    """Base Document Type View"""

    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permission_classes = [IsStaffPermission]
