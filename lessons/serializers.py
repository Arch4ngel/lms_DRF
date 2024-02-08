from rest_framework import serializers

from lessons.models import Course, Lesson, Payment, Subscription
from lessons.validators import LinkValidator


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'course', 'image', 'description', 'video_url']
        validators = [LinkValidator(fields='video_url')]


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    lessons_count = serializers.SerializerMethodField
    lessons = LessonSerializer(source='lesson_set', many=True)
    subscription = SubscriptionSerializer(source='subscription_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['name', 'image', 'description']

    def get_lesson_count(self, obj):
        return obj.lesson_set.all().count()

    def get_subscription(self, obj):
        return obj.subscription_set.all()


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['course', 'lesson', 'amount', 'method']
