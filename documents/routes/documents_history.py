from django.urls import path

from documents.views import (
    DocumentHistoryDetailView,
    DocumentsHistoryListView,
    DocumentVersionUpdateView,
)

app_name = "documents-history"

urlpatterns = [
    # Documents History
    path("history/", DocumentsHistoryListView.as_view(), name="documents-history-list"),
    path(
        "versions/<str:id>/",
        DocumentHistoryDetailView.as_view(),
        name="document-versions",
    ),
    path(
        "documents/update-from-history/",
        DocumentVersionUpdateView.as_view(),
        name="document-version-update",
    ),
]
