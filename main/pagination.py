from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        r = self.get_html_context()
        r['results'] = data
        r['count'] = self.page.paginator.count
        return Response(r)
