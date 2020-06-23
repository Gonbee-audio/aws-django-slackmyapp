from django.urls import path
from . import views
from rest_framework import routers
from .views import ChatMessageViewSet

router = routers.DefaultRouter()
router.register('chatmessage', ChatMessageViewSet)
urlpatterns = router.urls 