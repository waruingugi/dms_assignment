from django.urls import include, path

from documents.routes import document_types, documents, documents_history

urlpatterns = [
    path("", include(documents.urlpatterns)),
    path("", include(document_types.urlpatterns)),
    path("", include(documents_history.urlpatterns)),
]
