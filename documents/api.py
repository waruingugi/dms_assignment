from django.urls import include, path

from documents.routes import document_types, documents

urlpatterns = [
    path("", include(documents.urlpatterns)),
    path("", include(document_types.urlpatterns)),
]
