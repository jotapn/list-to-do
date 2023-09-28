from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Card


@receiver(pre_save, sender=Card)
def update_completed_at(sender, instance, **kwargs):
    if instance.status == 'done' and not instance.completed_at:
        instance.completed_at = timezone.now()
