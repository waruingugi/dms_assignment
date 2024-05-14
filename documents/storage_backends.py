from storages.backends.s3boto3 import S3Boto3Storage

from dms import settings


class DocumentStorage(S3Boto3Storage):
    """Define S3 Document Storage"""

    location = settings.DOCUMENT_LOCATION
    default = "public-read"
    file_overwrite = FileExistsError


class PublicMediaStorage(S3Boto3Storage):
    """Define public media storage"""

    location = settings.PUBLIC_MEDIA_LOCATION
    default_acl = "public-read"
    file_overwrite = False
