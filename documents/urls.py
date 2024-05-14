from django.urls import path

from documents.views import (
    DocumentDeleteAPIView,
    DocumentListAPIView,
    DocumentRetrieveUpdateAPIView,
    DocumentTypeCreateView,
    DocumentTypeDeleteAPIView,
    DocumentTypeListAPIView,
    DocumentTypeRetrieveUpdateAPIView,
    DocumentUploadView,
)

app_name = "documents"

urlpatterns = [
    # Documents
    path("upload/", DocumentUploadView.as_view(), name="document-upload"),
    path("list/", DocumentListAPIView.as_view(), name="document-list"),
    path(
        "document/<str:id>/",
        DocumentRetrieveUpdateAPIView.as_view(),
        name="document-detail",
    ),
    path(
        "document/<str:id>/delete/",
        DocumentDeleteAPIView.as_view(),
        name="document-delete",
    ),
    # Document Types
    path(
        "document-types/create/",
        DocumentTypeCreateView.as_view(),
        name="create-document-type",
    ),
    path(
        "document-types/list/",
        DocumentTypeListAPIView.as_view(),
        name="document-type-list",
    ),
    path(
        "document-types/<str:id>/",
        DocumentTypeRetrieveUpdateAPIView.as_view(),
        name="document-type-detail",
    ),
    path(
        "document-types/<str:id>/delete/",
        DocumentTypeDeleteAPIView.as_view(),
        name="document-type-delete",
    ),
]
