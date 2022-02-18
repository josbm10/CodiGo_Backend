
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bookmark

# Create your tests here.

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

class BookmarkModelTests(APITestCase):
    
    def test_create_bookmark(self):
        user1=User.objects.create_user(username='admin',password='admin')
        bk=Bookmark()
        bk.title='GOOGLE'
        bk.url='http://www.google.com'
        bk.access='public'
        bk.user=user1
        bk.save()
        
        self.assertEqual(bk.title,'GOOGLE')
        
        
class BookmarkAPIViewTests(APITestCase):
    
    def test_bookmark_post(self):
        user1=User.objects.create_user(username='admin',password='admin')
        url=reverse('app:bookmark')
        data={
            'title':'nuevo bookmark',
            'url':'http://www.google.com',
            'asccess':'public',
            'user':'1'
        }
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,200)
        self.assertEqual(Bookmark.objects.count(),1)
        self.assertEqual(Bookmark.objects.get().title,'nuevo bookmark')