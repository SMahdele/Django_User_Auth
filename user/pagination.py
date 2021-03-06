from rest_framework.pagination import PageNumberPagination


class UserProjectViewPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 2
    max_page_size = 5

class UserExperienceViewPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size=2
    max_page_size = 5

class UserEducationViewPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 5
    page_size=2
