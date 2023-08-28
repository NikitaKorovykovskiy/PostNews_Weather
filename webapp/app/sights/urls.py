from django.urls import path
from sights.views import sights_import

urlpatterns = [
    path("sight/import/", sights_import, name="sights_import"),
]
