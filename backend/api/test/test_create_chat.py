from rest_framework.test import APITestCase, APIClient


TITLE_MAX_LEN = 200


class TestCreateChat(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = '/chats/'
        cls.client = APIClient()

    def testCorrectCreate(self):
        title = 'Shadow wizard money gang'
        data = {
            'title': title
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 201)
        self.assertSetEqual(
            set(response.data.keys()),
            {'id', 'title', 'created_at'}
        )
        self.assertEqual(response.data['title'], title)

    def testTitleLimit(self):
        title = 'c' * (TITLE_MAX_LEN + 1)
        data = {
            'title': title
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 400)

    def testEmptyTitle(self):
        title = ''
        data = {
            'title': title
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 400)

    def testNoTitle(self):
        data = dict()

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 400)
