from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (SHNKSystemModelViewSet,
                    SHNKSubSystemsModelViewSet,
                    SHNKGroupsModelViewSet)

router = DefaultRouter()


router.register(r'systems', SHNKSystemModelViewSet)
router.register(r'groups', SHNKGroupsModelViewSet)
router.register(r'subsystems', SHNKSubSystemsModelViewSet)

urlpatterns = router.urls