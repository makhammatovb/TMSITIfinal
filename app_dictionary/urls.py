from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import DictionaryViewSet, WordViewset

router = DefaultRouter()

router.register(r'dictionary', DictionaryViewSet)
router.register(r'word', WordViewset)

urlpatterns = router.urls