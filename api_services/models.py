from django.db import models
from model_utils.models import TimeStampedModel


class FileDetail(TimeStampedModel):
    document = models.ForeignKey('file_upload.Document', on_delete=models.CASCADE, related_name='file_detail')
    line_number = models.IntegerField(default=0, null=True, blank=True)
    line_content = models.TextField(null=True, blank=True)
    line_length = models.IntegerField(default=0)
    most_occurred_letter = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        verbose_name = 'File Detail'
        verbose_name_plural = 'File Details'
        ordering = ('-line_length',)

    def to_dict(self):
        return {'file_name': self.document.filename(), 'line_length': self.line_length,
                'most_occurred_letter': self.most_occurred_letter, 'line_number': self.line_number,
                'line_content': self.line_content}

    def __str__(self):
        return f'{self.document.file.name} - {self.line_number} - {self.line_content} - {self.most_occurred_letter}'
