from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPageNumberPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        try:
            previous_number = self.page.previous_page_number()
        except:
            previous_number = None
        try:
            next_number = self.page.next_page_number()
        except:
            next_number = None
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('previous', self.get_previous_link()),
            ('previous_number', previous_number),
            ('current', self.page.number),
            ('next_number', next_number),
            ('next', self.get_next_link()),
            ('results', data)
        ]))
