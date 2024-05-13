from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from authentication.models import User


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Create authentication token after saving a new user"""
    if created:
        Token.objects.create(user=instance)  # type: ignore
