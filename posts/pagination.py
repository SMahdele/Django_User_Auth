from rest_framework.pagination import CursorPagination , PageNumberPagination

class PostsPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 5
    max_page_size = 10


class CommentsPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 5
    max_page_size = 10
