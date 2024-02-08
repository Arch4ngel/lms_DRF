from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lessons.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@sky.pro',
            is_staff=True,
            is_active=True,
            is_superuser=False,
            first_name='Petr',
            last_name='Petrov'

        )
        self.user.set_password('12345')
        self.user.save()
        self.course = Course.objects.create(
            name='test1',
            description='test1',

        )
        self.lesson_data = Lesson.objects.create(
            name='test1',
            description='test1',
            video_url='https://youtube.com/anyvideo',
            user=self.user,
            course=self.course
        )

    def test_lesson_create(self):
        """Test lesson creation"""
        response = self.client.post(
            '/lessons/lesson_create/',
            data={'pk': 2, 'name': 'test1', 'description': 'test1', 'course': self.course.pk, 'user': self.user.id,
                  'video_url': 'https://youtube.com/anyvideo'}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'pk': 4, 'name': 'test1', 'description': 'test1', 'course': self.course.pk, 'user': self.user.id,
             'video_url': 'https://youtube.com/anyvideo'}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_lesson(self):
        """Test Lesson List"""

        response = self.client.get(
            '/lesson/lesson/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'name': 'test1', 'description': 'test1',
                                                                      'course': self.course.pk, 'user': self.user.id,
                                                                      'video_url': 'https://youtube.com/anyvideo'}]})

    def test_delete(self):
        """Удаление урока"""

        response = self.client.delete(
            '/lessons/lesson_delete/1/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update(self):
        """обновление урока"""
        data = {'pk': 1, 'name': 'test1234', 'description': 'test1', 'course': self.course.pk,
                'user': self.user.id, 'video_url': 'https://youtube.com/anyvideo'}

        response = self.client.put(
            '/lessons/lesson_update/1/',
            data=data
        )

        self.assertEquals(response.json(),
                          {'pk': 1, 'name': 'test1234', 'description': 'test1', 'course': self.course.pk,
                           'user': self.user.id, 'video_url': 'https://youtube.com/anyvideo'}
                          )


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='test1',
            description='test1',

        )

        self.user = User.objects.create(
            email='test@sky.pro',
            is_staff=True,
            is_active=True,
            is_superuser=False,
            first_name='Petr',
            last_name='Petrov'

        )
        self.user.set_password('12345')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.subscribe = Subscription.objects.create(
            user=self.user,
            is_active=True,
            course=self.course
        )

    def test_create_subscribe(self):
        response = self.client.post(
            '/lessons/subscription/',
            data={'user': self.user.pk, 'is_active': True, 'course': self.course.pk}
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'is_active': True, 'user': self.user.pk, 'course': self.course.pk}

        )

    def test_subscribe_list(self):
        """Test List"""

        response = self.client.get(
            '/lesson/subscription/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.json(),
            [{'id': 1, 'is_active': True, 'user': self.user.pk, 'course': self.course.pk}]
        )

    def test_update(self):
        """обновление урока"""
        response = self.client.post(
            '/lesson/subscribe/',
            data={'user': self.user.pk, 'is_active': True, 'course': self.course.pk}
        )
        print(response.json())
        response = self.client.put(
            '/lesson/subscription/1/',

        )

        self.assertEquals(response.json(),
                          {'id': 1, 'is_active': True, 'user': 1, 'course': 1}

                          )

    def test_delete_subscription(self):
        response = self.client.post(
            '/lesson/subscription/',
            data={'user': self.user.pk, 'is_active': True, 'course': self.course.pk}
        )
        print(response.json())
        response = self.client.delete(
            '/lesson/subscription/2/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
