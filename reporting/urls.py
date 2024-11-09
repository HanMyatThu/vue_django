from django.urls import path, include
from reporting.views import OrderViewSet, ReportingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('reporting/', ReportingViewSet.as_view(), name='reporting'),
    path('', include(router.urls))
]