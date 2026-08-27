from django.test import TestCase
from django.urls import reverse

from .models import Course, Service, ContactMessage, Statistic


class PageTests(TestCase):

    def setUp(self):

        self.course = Course.objects.create(
            title='Python Programming',
            description='Learn Python programming.',
            icon='bi bi-filetype-py',
            price=1200,
            level='Beginner',
            hours=24,
            lectures=8,
            is_featured=True,
            is_active=True,
        )

        self.service = Service.objects.create(
            title='Web Development',
            description='Professional web development services.',
            icon='bi bi-globe',
            is_featured=True,
            is_active=True,
        )

        Statistic.objects.create(
            title='Students',
            value='100+',
            icon='bi bi-people',
            is_active=True,
            order=1,
        )


    def test_home_page(self):

        response = self.client.get(
            reverse('home')
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Python Programming'
        )

        self.assertContains(
            response,
            'Web Development'
        )

        self.assertContains(
            response,
            '100+'
        )


    def test_courses_page(self):

        response = self.client.get(
            reverse('courses')
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Python Programming'
        )


    def test_course_detail_page(self):

        response = self.client.get(
            reverse(
                'course_detail',
                args=[self.course.id]
            )
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Python Programming'
        )


    def test_services_page(self):

        response = self.client.get(
            reverse('services')
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Web Development'
        )


    def test_service_detail_page(self):

        response = self.client.get(
            reverse(
                'service_detail',
                args=[self.service.id]
            )
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Web Development'
        )


    def test_contact_page(self):

        response = self.client.get(
            reverse('contact')
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Contact Us'
        )


class ContactMessageTests(TestCase):

    def test_contact_form_creates_message(self):

        data = {
            'name': 'Radwa',
            'email': 'test@example.com',
            'subject': 'Test Message',
            'message': 'This is a test message.',
        }

        response = self.client.post(
            reverse('contact'),
            data
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            ContactMessage.objects.count(),
            1
        )

        message = ContactMessage.objects.first()

        self.assertEqual(
            message.name,
            'Radwa'
        )

        self.assertEqual(
            message.subject,
            'Test Message'
        )

        self.assertFalse(
            message.is_read
        )