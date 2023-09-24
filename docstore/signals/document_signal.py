from django.conf import settings
# from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from docstore.models import Document


@receiver(post_save, sender=Document)
def send_file_upload_notification(sender, instance, created, **kwargs):
    if created:
        subject = "File Upload Notification"
        message = f'The file "{instance.name}" was successfully uploaded.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.created_by.email]
        # send_mail(subject, message, from_email, recipient_list)
