from django.urls import path

from documents.views import DocumentTypeCreateView, DocumentUploadView

app_name = "documents"

urlpatterns = [
    path("upload/", DocumentUploadView.as_view(), name="document-upload"),
    path(
        "document-types/create/",
        DocumentTypeCreateView.as_view(),
        name="create-document-type",
    ),
]
