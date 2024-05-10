from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (AnnouncementsView,
                    NewsView,
                    NewsDetailView,
                    LeadershipView,
                    UnitsView,
                    StandardsView,
                    StandardsInformationView
)

router = DefaultRouter()
router.register(r'news', NewsView)
router.register(r'announcements', AnnouncementsView)
router.register(r'newsdetail', NewsDetailView)
router.register(r'leadership', LeadershipView)
router.register(r'units', UnitsView)
router.register(r'standards', StandardsView)
router.register(r'standardsinformation', StandardsInformationView)

urlpatterns = router.urls

