#from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import StreamPlatfrom ,WatchList, Review

class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='Big#&boy32', is_staff=True)
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream =StreamPlatfrom.objects.create(name="XYZABC",about="This is XYZABC",website="https://example.com/")

    def test_streamplatform_create(self):
        data={
            "name":"XYZABC",
            "about":"This is XYZABC",
            "website":"https://example.com/",
        }
        response=self.client.post(reverse('stream'),data)
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)

    def test_streamplatform_list(self):
        response=self.client.get(reverse('stream'))
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_streamplatform_ind(self):
        response=self.client.get(reverse('streamdetails',args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WactchlistTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='example', password='Big#&boy32', is_staff=True)
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream =StreamPlatfrom.objects.create(name="XYZABC",about="This is XYZABC",website="https://example.com/")
        self.watchlist= WatchList.objects.create(title="The Great",
            storyline="It's about the great movie!!",
            StreamingPlatform=self.stream,
            active=True)
    def test_watchlist_create(self):
        data={
            "title":"The Great",
            "storyline":"It's about the great movie!!",
            "StreamingPlatform":self.stream.name,
            "active":True
        }
        response=self.client.post(reverse('watch'),data=data)
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_watchlist(self):
        response=self.client.get(reverse('watch'))
        self.assertEqual(response.status_code ,status.HTTP_200_OK)

    def test_watchlist_indi(self):
        reponse=self.client.get(reverse('watchdetails',args=(self.watchlist.id,)))
        self.assertEqual(reponse.status_code ,status.HTTP_200_OK)
        self.assertEqual(WatchList.objects.get().title,'The Great')
        self.assertEqual(WatchList.objects.count(),1)

class ReviewTestCases(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='Big#&boy32', is_staff=True)
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream =StreamPlatfrom.objects.create(name="XYZABC",about="This is XYZABC",website="https://example.com/")
        self.watchlist= WatchList.objects.create(title="The Great",
            storyline="It's about the great movie!!",
            StreamingPlatform=self.stream,
            active=True)
        self.watchlist2= WatchList.objects.create(title="The Great Dan Of Kings",
            storyline="It's about the great movie!!",
            StreamingPlatform=self.stream,
            active=True)
        self.review = Review.objects.create(review_user=self.user ,rating=5,description="This was a reveiew",watchlist=self.watchlist2 , active=True )

    def test_review_create(self):
        data={
            "review_user":self.user,
            "rating":5,
            "description":"This was a reveiew",
            "watchlist":self.watchlist,
            "active":True
        }
        
        response = self.client.post(reverse("review-create", args=(self.watchlist.id,)),data)
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)

        response = self.client.post(reverse("review-create", args=(self.watchlist.id,)),data)
        self.assertEqual(response.status_code , status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauth(self):
        data={
            "review_user":self.user,
            "rating":5,
            "description":"This was a reveiew",
            "watchlist":self.watchlist,
            "active":True
        }

        self.client.force_authenticate(user=None)
        response=self.client.post(reverse('review-create',args=(self.watchlist.id,)),data)
        self.assertEqual(response.status_code , status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data={
           "review_user":self.user,
            "rating":4,
            "description":"This was a reveiew",
            "watchlist":self.watchlist,
            "active":True 
        }

        response= self.client.put(reverse('reviews_specific', args=(self.watchlist.id,)),data=data)
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_review_list(self):
        response=self.client.get(reverse('review-list',args=(self.watchlist.id,)))
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_review_list_indi(self):
        response=self.client.get(reverse('review_user',args=(self.review.id,)))
        self.assertEqual(response.status_code , status.HTTP_200_OK)
