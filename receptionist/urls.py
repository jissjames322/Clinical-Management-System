from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, MembershipViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'memberships', MembershipViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
