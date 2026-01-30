from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from messages.models import Chat, Message
from api.paginators import BasicLimitPagination


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = (
            'id',
            'title',
            'created_at'
        )
        read_only_fields = (
            'id',
            'created_at'
        )


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields =  (
            'id',
            'chat_id',
            'text',
            'created_at'
        )
        read_only_fields = (
            'id',
            'chat_id',
            'created_at'
        )
    
    def create(self, validated_data):
        chat_id = self.context.get('chat_id')
        if not chat_id:
            raise ValidationError('Не найден id чата в контексте.')

        validated_data['chat_id'] = get_object_or_404(Chat, pk=chat_id)
        return super().create(validated_data)


class ChatWithRelatedSerializer(serializers.ModelSerializer):
    chat = ChatSerializer(read_only=True, source='*')
    messages = serializers.SerializerMethodField('get_paginated_messages')

    def get_paginated_messages(self, obj):
        paginator = BasicLimitPagination()
        limited_messages = paginator.paginate_queryset(
            obj.messages.all(),
            self.context['request']
        )
        serializer = MessageSerializer(limited_messages, many=True, context=self.context)
        return serializer.data

    class Meta:
        model = Chat
        fields = (
            'chat',
            'messages'
        )

