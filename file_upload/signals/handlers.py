from django.db.models.signals import post_save
from django.dispatch import receiver

from api_services.models import FileDetail
from .. import models
from ..domain import detail_info_extractor as ds


@receiver(post_save, sender=models.Document)
def save_details_upon_file_save(sender, instance, created, **kwargs):
    """
    This signal will parse the file and try to save the line_content,
    line_length, etc. to file details model.
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        file_object = models.Document.objects.latest('created')
        file_context = ds.create_file_content_list(file=file_object.file)
        if file_context:
            for file_detail in file_context:
                FileDetail.objects.get_or_create(document=file_object,
                                                 line_number=file_detail.line_number,
                                                 line_content=file_detail.line_content,
                                                 line_length=file_detail.line_length,
                                                 most_occurred_letter=file_detail.most_occurred_letter,
                                                 )
