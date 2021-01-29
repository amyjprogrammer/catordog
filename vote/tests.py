from datetime import datetime
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from .models import Question, Choice
from .views import home, vote, results, resultsData

# Create your tests here.

class QuestionTest(TestCase):

    def setUp(self):
        #testing number of choices
        question="What is your favourite color?"
        now = datetime.now()
        self.question = Question.objects.create(question_text=question, pub_date=now)
        self.question.choice_set.create(choice_text="Red", votes=1)
        self.question.choice_set.create(choice_text="Bue", votes=1)
        self.question.choice_set.create(choice_text="Green", votes=1)

    def test_models_choice_set(self):
        self.assertEqual(self.question.choice_set.all().count(), 3)

#testing my urlpatterns
class TestUrls(SimpleTestCase):

    def test_home_view_url(self):
        url = reverse('vote:home')
        self.assertEquals(resolve(url).func, home)

    def test_vote_view_url(self):
        url = reverse('vote:vote', args= [1] )
        self.assertEquals(resolve(url).func, vote)

    def test_results_view_url(self):
        url = reverse('vote:results', args= [1] )
        self.assertEquals(resolve(url).func, results)

    def test_resultsdata_view_url(self):
        url = reverse('vote:resultsdata', args= [1] )
        self.assertEquals(resolve(url).func, resultsData)

#testing template used and no error code
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('vote:home')


    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote/home.html')
