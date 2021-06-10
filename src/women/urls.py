from django.urls import path, re_path
from women.views import *

urlpatterns = [
    path('', index),  # site/women
    path('about', about),
    path('cats/<int:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
