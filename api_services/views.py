from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import ugettext as _

from .domain.helpers import get_http_accept_list as gha, check_http_accept_and_create_response_accordingly as chs
from .domain.data_fetching import get_random_line_from_latest_file as dc, get_random_line_backward as dbc, \
    get_hundreds_longest_lines as hll, get_twenty_longest_lines_from_latest_file as gll

NO_LINE_MSG = _('No lines found')
ERROR_MSG = _('Server Error')


def get_one_line(request):
    try:
        accept_list = gha(request.META.get('HTTP_ACCEPT'))
        res = chs(accept_list=accept_list)
        return res
    except Exception as error:
        print(error)
        return JsonResponse({'msg': ERROR_MSG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OneRandomLineBackwards(APIView):
    """
    As we are keeping this endpoints open we will not add any permission or
    authentication classes.
    And as to accept header thingy is not specified here, I would assume
    json response would be fine here
    """
    permission_classes = []
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            one_r_line_backward = dbc(dc())
            msg = _('random line backward')
            return Response({msg: one_r_line_backward})
        except Exception as e:
            print(e)
            return Response({'msg': ERROR_MSG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HundredsLongestLines(APIView):
    """
    As we are keeping this endpoints open we will not add any permission or
    authentication classes.
    And as to accept header thingy is not specified here, I would assume
    json response would be fine here
    """
    permission_classes = []
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            longest_100_lines = hll()
            if hundreds_longest_line:
                return Response(longest_100_lines)
            return Response({'msg': NO_LINE_MSG})
        except Exception as e:
            print(e)
            return Response({'msg': ERROR_MSG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TwentyLongestLinesOfLastFile(APIView):
    """
    As we are keeping this endpoints open we will not add any permission or
    authentication classes.
    And as to accept header thingy is not specified here, I would assume
    json response would be fine here
    """
    permission_classes = []
    authentication_classes = []

    @staticmethod
    def get(request):
        try:
            twenty_lines = gll()
            if twenty_lines:
                return Response(twenty_lines)
            return Response({'msg': NO_LINE_MSG})
        except Exception as e:
            print(e)
            return Response({'msg': ERROR_MSG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


one_random_line_backwards = OneRandomLineBackwards.as_view()
twenty_longest_line_of_last_file = TwentyLongestLinesOfLastFile.as_view()
hundreds_longest_line = HundredsLongestLines.as_view()
