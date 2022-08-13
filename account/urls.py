from django.contrib import admin
from django.urls import path, include
from .views import (
    ProfileListApiView,
)

urlpatterns = [
    path('api', ProfileListApiView.as_view()),
    path('', ProfileListApiView.as_view()),
]
