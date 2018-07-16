from django.urls import include, patterns

urlpatterns = patterns(
    '',
    (r'^markdown/', include('django_markdown.urls')),
)
