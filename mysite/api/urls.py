from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import movieViewSet

router = routers.DefaultRouter()
router.register('movie', movieViewSet)
urlpatterns = router.urls
