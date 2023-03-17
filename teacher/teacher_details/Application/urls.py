from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import teacher, TeacherModelViewSet,logout

router = routers.DefaultRouter()

router.register(r"teacher", TeacherModelViewSet, basename="teacher-view")

urlpatterns = [
    path("", include(router.urls)),
    path('login', teacher),
    path('logout/', logout)]