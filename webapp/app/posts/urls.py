from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet, basename="posts")

urlpatterns = [
    path("api/", include(router.urls)),
]
