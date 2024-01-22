from rest_framework import serializers

from lessons.models import Course, Lesson


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'image', 'description']


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'image', 'description', 'video_url']
