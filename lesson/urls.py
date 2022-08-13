from django.contrib import admin
from django.urls import path, include
from .views import (
    LessonListApiView,
)

urlpatterns = [
    path('api', LessonListApiView.as_view()),
    path('', LessonListApiView.as_view()),
]
