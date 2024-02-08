from django.urls import path
from rest_framework import routers

from lessons.views import *
from lessons.apps import LessonsConfig

appname = LessonsConfig.name

router_course = routers.DefaultRouter()
router_payment = routers.DefaultRouter()
router_subscription = routers.DefaultRouter()

router_course.register(r'lessons', CourseViewSet, basename='course')
router_payment.register(r'lessons', PaymentViewSet, basename='payment')
router_subscription.register(r'lessons', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('lesson_create', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson_list', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson'),
    path('lesson_update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson_delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
] + router_course.urls + router_payment.urls + router_subscription.urls
