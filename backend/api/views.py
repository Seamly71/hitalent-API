from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.exceptions import ValidationError

from api.serializers import ChatSerializer, MessageSerializer, ChatWithRelatedSerializer
from messages.models import Chat, Message


class ChatViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        if self.action in {'retrieve', }:
            return Chat.objects.prefetch_related('messages')
        return Chat.objects.all()

    def get_serializer_class(self):
        if self.action in {'retrieve',}:
            return ChatWithRelatedSerializer
        return ChatSerializer


class MessageViewSet(
    CreateModelMixin,
    GenericViewSet
):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()

        chat_id = self.kwargs.get('id')
        if not chat_id:
            raise ValidationError('Не найден id чата в url.')

        context['chat_id'] = chat_id
        return context