from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from random import randrange


from .models import Contact
from .serialisers import ContactSerialiser
# Create your tests here.

class ContactListTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 25 contacts for pagination tests
        number_of_contacts = 25

        for contact_id in range(number_of_contacts):
            Contact.objects.create(
                firstname = f'Jonathan{contact_id}',
                lastname = f'Nalo {contact_id}',
                phone = f'0245{randrange(100000,300000)}'
            )

        print(Contact.objects.all().count())
        print(Contact.objects.get(pk=1).phone)
        print(ContactSerialiser.objects.count())
    
    def test_pagination(self):
        response = self.client.get(reverse('list_contacts'))
        self.assertEqual(response.status_code, 200)
        #self.assertTrue('is_paginated' in response.context)
        #self.assertTrue(response.context['is_paginated'] == True)
        #self.assertEqual(len(response.context['contact_list']), 20)
        print(response.context)

# class ContactDetailTest(TestCase):
    
#     def setUp(self):
#         Contact.objects.create(name="lion", sound="roar")
#         Contact.objects.create(name="cat", sound="meow")

#     def test_contacts(self):
        
#         pass