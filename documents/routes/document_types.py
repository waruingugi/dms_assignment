from django.urls import path

from documents.views import (
    DocumentTypeCreateView,
    DocumentTypeDeleteAPIView,
    DocumentTypeListAPIView,
    DocumentTypeRetrieveUpdateAPIView,
)

app_name = "document-types"

urlpatterns = [
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
