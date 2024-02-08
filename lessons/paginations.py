from rest_framework.pagination import PageNumberPagination


class LessonCoursePagination(PageNumberPagination):
    page_size = 10
