from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
urlpatterns = router.urls
urlpatterns += [
    url(r"^get_repeated_elements/", get_repeated_elements),
]
