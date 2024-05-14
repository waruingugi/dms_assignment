from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from documents.models import DocumentType
from documents.serializers import DocumentSerializer, DocumentTypeSerializer


class DocumentUploadView(APIView):
    """Handle file uploads"""

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = DocumentSerializer

    def post(self, request, *args, **kwargs):
        """Upload a document"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            document = serializer.save(created_by=request.user)
            # Serialize the instance again to capture all fields including those set by the save method
            response_serializer = DocumentSerializer(document)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentTypeCreateView(CreateAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

    def get_serializer_context(self) -> dict:
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
