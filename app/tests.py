from django.test import TestCase, Client

# python manage.py dumpdata > fixtures.json

# Create your tests here.
class AuthorTestCase(TestCase):

    fixtures = ['fixtures2.json']

    def setUp(self):
        self.client = Client()

    def test_get_status_code(self):
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, 200)

    def test_get_response(self):
        response = self.client.get('/post/')
        self.assertIsInstance(response.data, list)

    def test_get_single_response(self):
        response = self.client.get('/post/?pk=1')
        print(response.data)
        test_response = {
            "id": 1,
            "author_id": 1,
            "title": "New Post",
            "text": "Post body edited second time",
            "created": "2020-11-09T17:02:05.187313Z",
            "updated": "2020-11-09T17:02:05.187369Z"
        }
        self.assertEqual(response.data, test_response)
    #
    # def test_get_incorrect_response(self):
    #     response = self.client.get('/authors/')
    #     self.assertNotEqual(response.data, {"response": 200, "false_data": 6})

