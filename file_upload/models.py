import os
import uuid

from django.db import models
from model_utils import Choices
from model_utils.models import TimeFramedModel, TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class Document(TimeFramedModel, TimeStampedModel):
    """
    This a TimeFrame and Timestamp model which means
    that it will automatically add created, modified, start and end fields.
    And those fields will enable us to track time of creation, modification
    of each file, and also we can save data in future or in past using start
    and end field.
    for more info please have a look at this doc
    https://django-model-utils.readthedocs.io/en/latest/models.html
    Besides, uuid - universally unique id has been used for the primary key, instead
    of auto generated integer id.
    """
    STATUS = Choices(
        'PARSED',
        'NON_PARSED'
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(_('description'), max_length=255, blank=True, null=True)
    file = models.FileField(_('file'), upload_to='file_upload_assets/')
    status = models.CharField(max_length=24,
                              choices=STATUS,
                              default=STATUS.NON_PARSED)

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return f'{self.filename()} saved in {self.file.name}'
