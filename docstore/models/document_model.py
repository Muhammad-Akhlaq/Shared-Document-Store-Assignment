import os
import uuid

from django.db import models

from docstore.models.base_model import BaseModel


def generate_filename(instance, filename):
    _, ext = os.path.splitext(filename)
    unique_filename = f'{uuid.uuid4()}{ext}'
    return os.path.join(f'documents/{instance.folder.name}_{instance.folder.pk}', unique_filename)


class Document(BaseModel):
    name = models.CharField(max_length=255, db_index=True)
    file = models.FileField(upload_to=generate_filename)
    folder = models.ForeignKey(
        "Folder", on_delete=models.CASCADE, related_name="documents"
    )
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
