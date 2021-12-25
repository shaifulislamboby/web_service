import logging

from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict

from api_services.models import FileDetail
from file_upload.models import Document
from django.utils.translation import ugettext as _


def fetch_all_entries_from_latest_file():
    """
    getting all the file details using reverse Django manager
    :return:
    """
    return Document.objects.latest('created').file_detail.all()


def get_random_line_from_latest_file():
    """
    This function will return one random line from last
    added file, given that the file is a txt file.
    :return:
    """
    file_details = fetch_all_entries_from_latest_file()
    if not file_details:
        return _('Last file that you uploaded could not be parsed')
    return model_to_dict(file_details.order_by('?').first())


def get_random_line_backward(line_dict) -> str:
    if isinstance(line_dict, dict):
        __line = reversed(line_dict.get('line_content').split(' '))
        return ' '.join(__line)
    return line_dict


def get_x_longest_lines(number_of_lines: int) -> dict:
    try:
        largest_lines = FileDetail.objects.all().values('line_content')[:number_of_lines]
        if largest_lines:
            return {[str(index)]: line.get('line_content') for index, line in enumerate(largest_lines)}
        return {}
    except ObjectDoesNotExist as error:
        print(error)
        return {}
