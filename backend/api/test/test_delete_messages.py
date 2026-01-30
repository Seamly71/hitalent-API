from rest_framework.test import APITestCase, APIClient

from messages.models import Chat, Message


class TestDeleteChat(APITestCase):

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

    def testCorrectDelete(self):
        response = self.client.delete(self.url.format(self.chat_id))

        self.assertEqual(response.status_code, 204)
        with self.assertRaises(Chat.DoesNotExist):
            Chat.objects.get(pk=self.chat_id)
        with self.assertRaises(Message.DoesNotExist):
            Message.objects.get(pk=self.message_first.id)
        with self.assertRaises(Message.DoesNotExist):
            Message.objects.get(pk=self.message_second.id)

    def testDeleteNonExistentChat(self):
        response = self.client.delete(self.url.format(self.chat_id + 1))

        self.assertEqual(response.status_code, 404)