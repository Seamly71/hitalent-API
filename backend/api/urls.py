from rest_framework.routers import SimpleRouter

from api.views import ChatViewSet, MessageViewSet


router = SimpleRouter()
router.register(r'chats/(?P<id>[1-9]\d*)/messages', MessageViewSet, 'messages')
router.register('chats', ChatViewSet, 'chats')

urlpatterns = router.urls

app_name = 'api'