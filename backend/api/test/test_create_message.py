from rest_framework.test import APITestCase, APIClient

from messages.models import Chat


TEXT_MAX_LEN = 5000


class TestCreateMessage(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = '/chats/{}/messages/'
        cls.client = APIClient()

    def setUp(self):
        self.chat = Chat.objects.create(
            title='Shadow wizard money gang'
        )
        self.chat_id = self.chat.id

    def testCorrectCreation(self):
        text = 'Wassup!'
        data = {
            'text': text
        }

        response = self.client.post(
            self.url.format(self.chat_id),
            data
        )

        self.assertEqual(response.status_code, 201)
        self.assertSetEqual(
            set(response.data.keys()),
            {'id', 'chat_id', 'text', 'created_at'}
        )
        self.assertEqual(response.data['chat_id'], self.chat_id)
        self.assertEqual(response.data['text'], text)

    def testTextLimit(self):
        text = 'c' * (TEXT_MAX_LEN + 1)
        data = {
            'text': text
        }

        response = self.client.post(
            self.url.format(self.chat_id),
            data
        )

        self.assertEqual(response.status_code, 400)

    def testEmptyText(self):
        text = ''
        data = {
            'text': text
        }

        response = self.client.post(
            self.url.format(self.chat_id),
            data
        )

        self.assertEqual(response.status_code, 400)

    def testMessageNonExistentChat(self):
        text = 'Wassup!'
        data = {
            'text': text
        }

        response = self.client.post(
            self.url.format(self.chat_id + 1),
            data
        )

        self.assertEqual(response.status_code, 404)

    def testMessageNoText(self):
        data = dict()

        response = self.client.post(
            self.url.format(self.chat_id),
            data
        )

        self.assertEqual(response.status_code, 400)
