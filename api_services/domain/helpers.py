import dicttoxml
from django.http import JsonResponse, HttpResponse

from .data_fetching import get_random_line_from_latest_file as dc

ACCEPT_JS = ['*/*', 'application/*', 'application/json']

ACCEPT_XML = ['application/xml', 'application/xhtml+xml']


def get_http_accept_list(http_accept):
    accept = http_accept.split(',')
    for i in accept[:]:
        accept.append(i.split(';')[0])
        accept.remove(i)
    return accept


def check_http_accept_and_create_response_accordingly(accept_list):
    msg = dc()
    if isinstance(msg, dict):
        if any(value in ACCEPT_JS for value in accept_list):
            return JsonResponse(msg)
        elif any(value in ACCEPT_XML for value in accept_list):
            return HttpResponse(dicttoxml.dicttoxml(msg), content_type='application/xml')
        else:
            return HttpResponse(msg.get('line_content'), content_type='text/plain')

    return []
