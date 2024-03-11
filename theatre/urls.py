from rest_framework import routers
from django.urls import include, path

from theatre.views import (
    ActorViewSet,
    GenreViewSet, PlayViewSet
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("plays", PlayViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
