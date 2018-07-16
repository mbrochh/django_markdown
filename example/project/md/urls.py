from django.urls import patterns, include, re_path

urlpatterns = patterns(
    '',
    re_path(r'^$', 'project.md.views.home'),
)
