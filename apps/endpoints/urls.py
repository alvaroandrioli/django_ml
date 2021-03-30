# backend/server/apps/endpoints/urls.py file
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import ABTestViewSet, EndpointViewSet, StopABTestView
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import MLRequestViewSet
from apps.endpoints.views import PredictView # import PredictView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")
router.register(r"abtests", ABTestViewSet, basename="abtests")

urlpatterns = [
  path(r"api/v1/", include(router.urls)),
  path(r"api/v1/<endpoint_name>/predict", PredictView.as_view(), name="predict"),
  path(r"api/v1/stop_ab_test/<ab_test_id>", StopABTestView.as_view(), name="stop_ab"),
]