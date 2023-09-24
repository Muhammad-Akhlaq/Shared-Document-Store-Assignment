from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    class Meta:
        abstract = True

    def is_owned_by(self, user):
        return self.created_by == user
