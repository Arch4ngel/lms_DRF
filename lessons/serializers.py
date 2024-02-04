from rest_framework import serializers

from lessons.models import Course, Lesson, Payment


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'course', 'image', 'description', 'video_url']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    lessons_count = serializers.SerializerMethodField
    lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = ['name', 'image', 'description']

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['course', 'lesson', 'amount', 'method']
