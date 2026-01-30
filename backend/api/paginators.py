from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from api.constants import DEFAULT_PAGINATION_LIMIT, MAX_PAGINATION_LIMIT


class BasicLimitPagination(LimitOffsetPagination):
    default_limit = DEFAULT_PAGINATION_LIMIT
    max_limit = MAX_PAGINATION_LIMIT

    def get_paginated_response(self, data):
        return Response(data)

    # Игнорируем оффсет.
    def get_offset(self, request):
        return 0