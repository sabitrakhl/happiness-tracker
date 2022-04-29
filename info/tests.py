from collections import OrderedDict

from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from info.models import User, HappinessInfo


class CreateInfoTest(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        self.client.login(username='testuser', password='12345')
        self.data = {'happiness_level': 5}

    def test_can_create_info(self):
        response = self.client.post(reverse('info-create-api'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RetrieveInfoTest(APITestCase):
    def setUp(self):
        group_a = Group.objects.create(name="GroupA")
        group_b = Group.objects.create(name="GroupB")

        user1 = User.objects.create(username='testuser1')
        user1.set_password('12345')
        user1.groups.add(group_a)
        user1.save()

        HappinessInfo.objects.create(user=user1, happiness_level=7)

        user2 = User.objects.create(username='testuser2')
        user2.set_password('12345')
        user2.groups.add(group_a)
        user2.save()

        HappinessInfo.objects.create(user=user2, happiness_level=7)

        user3 = User.objects.create(username='testuser3')
        user3.set_password('12345')
        user3.groups.add(group_a)
        user3.save()

        HappinessInfo.objects.create(user=user3, happiness_level=4)

        user4 = User.objects.create(username='testuser4')
        user4.set_password('12345')
        user4.groups.add(group_b)
        user4.save()

        HappinessInfo.objects.create(user=user4, happiness_level=2)

    def test_retrieve_info_with_no_auth(self):
        response = self.client.get(reverse('info-retrieve-api'))

        data = {
            "happiness_level__avg": 5
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    def test_retrieve_info_with_auth(self):
        self.client.login(username='testuser1', password='12345')

        response = self.client.get(reverse('info-retrieve-api'))

        data = {
            'happiness_level__avg': 6.0,
            'happiness_info': [
                OrderedDict([('level', 4), ('count', 1)]),
                OrderedDict([('level', 7), ('count', 2)]),
            ]
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
