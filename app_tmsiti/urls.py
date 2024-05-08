from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import AnnouncementsView, NewsView, NewsDetailView

router = DefaultRouter()
router.register(r'news', NewsView)
router.register(r'announcements', AnnouncementsView)
router.register(r'newsdetail', NewsDetailView)

urlpatterns = router.urls

