from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import friendship_view

urlpatterns = [
    path('friendships/', friendship_view),
]
