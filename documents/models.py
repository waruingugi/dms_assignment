from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from commons.base_model import Base
from dms.settings import DOCUMENT_LOCATION
from documents.storage_backends import DocumentStorage

User = get_user_model()


class DocumentType(Base):
    """Type of documents to be uploaded."""

    type = models.CharField(max_length=100, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=200, help_text=_("A brief description of the type of the document")
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.type


class Documents(Base):
    """Model where documents are uploaded"""

    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        User,
        related_name="deleted_documents",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_by = models.ForeignKey(
        User, related_name="created_documents", on_delete=models.CASCADE
    )
    patient = models.ForeignKey(
        User, related_name="patient_documents", on_delete=models.CASCADE
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text=_("Notes you would like to accompany this document"),
    )
    file = models.FileField(storage=DocumentStorage())
    history = HistoricalRecords()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("document")
        verbose_name_plural = _("documents")

    def save(self, *args, **kwargs):
        if self.file:
            patient_id = self.patient.id
            self.file.storage.location = f"{DOCUMENT_LOCATION}/{patient_id}/{self.id}"

        super(Documents, self).save(*args, **kwargs)
