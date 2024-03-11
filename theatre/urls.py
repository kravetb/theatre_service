from rest_framework import routers
from django.urls import include, path

from theatre.views import (
    ActorViewSet,
    GenreViewSet, PlayViewSet, PerformanceViewSet
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
