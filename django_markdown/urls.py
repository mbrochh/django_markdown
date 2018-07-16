""" Define preview URL. """

from django.urls import re_path

from .views import preview

urlpatterns = [re_path(r'preview/$', preview, name='django_markdown_preview')]
