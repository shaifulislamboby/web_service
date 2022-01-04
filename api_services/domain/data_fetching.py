import logging

from django.core.exceptions import ObjectDoesNotExist

from api_services.models import FileDetail
from file_upload.models import Document
from django.utils.translation import ugettext as _


def get_random_line_from_latest_file(*args, **kwargs):
    """
    This function will return one random line from last
    added file, given that the file is a txt file.
    :return:
    """
    try:
        one_line = Document.objects.latest('created').file_detail.order_by('?').first()
        if one_line:
            return one_line.to_dict()
        else:
            return _('Last file that you uploaded could not be parsed')
    except ObjectDoesNotExist:
        return _('Last file that you uploaded could not be parsed')


def get_random_line_backward(line_dict) -> str:
    if isinstance(line_dict, dict):
        return ' '.join(reversed(line_dict.get('line_content').split(' ')))
    return line_dict


def get_x_longest_lines(number_of_lines: int) -> dict:
    try:
        largest_lines = FileDetail.objects.values('line_content')[:number_of_lines]
        if largest_lines:
            return {str(index): line.get('line_content') for index, line in enumerate(largest_lines)}
        return {}
    except ObjectDoesNotExist as error:
        print(error)
        return {}
