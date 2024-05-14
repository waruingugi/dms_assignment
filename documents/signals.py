from django.dispatch import receiver
from simple_history.signals import post_create_historical_record


@receiver(post_create_historical_record)
def post_create_historical_record_callback(sender, **kwargs):
    """Over-write file url field"""
    history_instance = kwargs["history_instance"]
    model_instance = kwargs["instance"]

    history_instance.file = model_instance.file.url
    history_instance.save()