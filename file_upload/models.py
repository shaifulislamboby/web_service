import uuid

from django.db import models
from model_utils.models import TimeFramedModel, TimeStampedModel


class Document(TimeFramedModel, TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    location = models.FileField(upload_to='file_upload_assets/')

    def __str__(self):
        return f'{self.description} saved in {self.location}'
