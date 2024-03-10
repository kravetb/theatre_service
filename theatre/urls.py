from rest_framework import routers
from django.urls import include, path

from theatre.views import ActorViewSet

router = routers.DefaultRouter()
router.register("actors", ActorViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
