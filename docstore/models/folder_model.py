from django.db import models

from docstore.models.base_model import BaseModel


class Folder(BaseModel):
    name = models.CharField(max_length=255, db_index=True)
    parent_folder = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name
