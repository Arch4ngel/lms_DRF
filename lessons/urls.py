from django.urls import path
from rest_framework import routers

from lessons.views import *

router = routers.DefaultRouter()
router.register(r'lessons', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson_create', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson_list', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson'),
    path('lesson_update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson_delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
] + router.urls
