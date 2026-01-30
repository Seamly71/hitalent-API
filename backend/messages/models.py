from django.db import models
from .constants import CHAT_TITLE_MAX_LEN, MESSAGE_MAX_LEN, MESSAGE_CUTOFF


class Chat(models.Model):
    title = models.CharField(
        max_length=CHAT_TITLE_MAX_LEN,
        verbose_name='заголовок'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания'
    )

    class Meta:
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'

    def __str__(self):
        return self.title

class Message(models.Model):
    # Имя поля некорректное, но таково требование ТЗ.
    chat_id = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='чат'
    )
    text = models.TextField(
        max_length=MESSAGE_MAX_LEN,
        verbose_name='текст'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='время создания'
    )

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.created_at}: {self.text[:MESSAGE_CUTOFF]}'
