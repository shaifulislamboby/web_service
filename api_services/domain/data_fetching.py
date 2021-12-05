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
    return file_details.order_by('?').first().to_dict()


def get_random_line_backward(line_dict) -> str:
    if isinstance(line_dict, dict):
        __line = reversed(line_dict.get('line_content').split(' '))
        return ' '.join(__line)
    return line_dict


def get_hundreds_longest_lines():
    line_content_dict = {}
    try:
        largest_100_lines = FileDetail.objects.all().values('line_content')[:100]
        if largest_100_lines:
            index = 1
            for line in largest_100_lines:
                line_content_dict[str(index)] = line.get('line_content')
                index += 1
        return line_content_dict
    except Exception as error:
        print(error)
        return line_content_dict


def get_twenty_longest_lines_from_latest_file():
    twenty_line_dict = {}
    try:
        largest_20_lines = fetch_all_entries_from_latest_file().values('line_content')[0:20]
        if largest_20_lines:
            index = 1
            for line in largest_20_lines:
                twenty_line_dict[str(index)] = line.get('line_content')
                index += 1
        return twenty_line_dict
    except Exception as error:
        print(error)
        return twenty_line_dict
