from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 7
    last_page_strings = 'end'

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 7

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'name'
    cursor_query_param = 'cu' 