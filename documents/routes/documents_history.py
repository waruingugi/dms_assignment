from django.urls import path

from documents.views import DocumentHistoryDetailView, DocumentsHistoryListView

app_name = "documents-history"

urlpatterns = [
    # Documents History
    path("history/", DocumentsHistoryListView.as_view(), name="documents-history-list"),
    path(
        "versions/<str:id>/",
        DocumentHistoryDetailView.as_view(),
        name="document-versions",
    ),
]
