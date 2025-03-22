from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Contact



@receiver(post_save, sender=Contact, dispatch_uid="contact_created")
def contact_was_created(sender, instance, created, **kwargs):
    """Send a signal when a contact is created."""
    print("\nContact created.\n")
    if created:
        print("created.")