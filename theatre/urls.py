from rest_framework import routers
from django.urls import include, path

from theatre.views import (
    ActorViewSet,
    GenreViewSet,
    PlayViewSet,
    PerformanceViewSet,
    TheatreHallViewSet, ReservationViewSet,
)

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("theatre_hall", TheatreHallViewSet)
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
