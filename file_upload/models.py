import uuid

from django.db import models
from model_utils.models import TimeFramedModel, TimeStampedModel


class Document(TimeFramedModel, TimeStampedModel):
    """
    This a TimeFrame and Timestamp model which means
    that it will automatically add created, modified, start and end fields.
    And those fields will enable us to track time of creation, modification
    of each file.
    Besides, uuid - universally unique id has been used for the primary key, instead
    of auto generated integer id.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='file_upload_assets/')

    def __str__(self):
        return f'{self.description} saved in {self.file}'
