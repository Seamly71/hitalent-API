from rest_framework.test import APIClient, APITestCase

from messages.models import Chat, Message


class TestListMessages(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.url = '/chats/{}/'
        cls.client = APIClient()

    def setUp(self):
        self.chat = Chat.objects.create(
            title='Shadow wizard money gang'
        )
        self.chat_id = self.chat.id
        self.message_first = Message.objects.create(
            chat_id=self.chat,
            text='Wazzap!'
        )
        self.message_second = Message.objects.create(
            chat_id=self.chat,
            text='Hi!'
        )

    def testCorrectList(self):
        response = self.client.get(self.url.format(self.chat_id))

        self.assertEqual(response.status_code, 200)
        self.assertSetEqual(
            set(response.data.keys()),
            {'chat', 'messages'}
        )
        self.assertIsInstance(response.data['chat'], dict)
        self.assertSetEqual(
            set(response.data['chat'].keys()),
            {'id', 'title', 'created_at'}
        )
        self.assertIsInstance(response.data['messages'], list)
        for message in response.data['messages']:
            self.assertIsInstance(message, dict)
            self.assertSetEqual(
                set(message.keys()),
                {'id', 'chat_id', 'text', 'created_at'}
            )
        self.assertEqual(len(response.data['messages']), 2)

    def testPagination(self):
        response = self.client.get(
            self.url.format(self.chat_id),
            query_params={'limit': 1}
        )

        self.assertEqual(response.status_code, 200)
        self.assertSetEqual(
            set(response.data.keys()),
            {'chat', 'messages'}
        )
        self.assertIsInstance(response.data['chat'], dict)
        self.assertSetEqual(
            set(response.data['chat'].keys()),
            {'id', 'title', 'created_at'}
        )
        self.assertIsInstance(response.data['messages'], list)
        for message in response.data['messages']:
            self.assertIsInstance(message, dict)
            self.assertSetEqual(
                set(message.keys()),
                {'id', 'chat_id', 'text', 'created_at'}
            )
        self.assertEqual(len(response.data['messages']), 1)

    def testNonExistentChat(self):
        response = self.client.get(
            self.url.format(self.chat_id + 1)
        )

        self.assertEqual(response.status_code, 404)