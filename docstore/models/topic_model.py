from django.db import models

from docstore.models.base_model import BaseModel


class Topic(BaseModel):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name
