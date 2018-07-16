""" Define preview URL. """

from django.urls import patterns, re_path

from .views import preview

urlpatterns = patterns(
    '', re_path('preview/$', preview, name='django_markdown_preview'))
