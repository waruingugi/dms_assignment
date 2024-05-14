from django.urls import path

from documents.views import (
    DocumentDeleteAPIView,
    DocumentListAPIView,
    DocumentRetrieveUpdateAPIView,
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
]
