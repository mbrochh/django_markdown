""" Markdown utils. """
from django.urls import reverse
import markdown as markdown_module
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe
from django.template import loader, Context

try:
    import json as simplejson
except ImportError:
    try:
        import simplejson
    except ImportError:
        from django.utils import simplejson

from . import settings


def markdown(value,
             extensions=settings.MARKDOWN_EXTENSIONS,
             extension_configs=settings.MARKDOWN_EXTENSION_CONFIGS,
             safe=False):
    """ Render markdown over a given value, optionally using varios extensions.

    Default extensions could be defined which MARKDOWN_EXTENSIONS option.

    :returns: A rendered markdown

    """
    return mark_safe(
        markdown_module.markdown(
            force_str(value),
            extensions=extensions,
            extension_configs=extension_configs,
            safe_mode=safe))


def editor_js_initialization(selector, **extra_settings):
    """ Return script tag with initialization code. """

    INIT_TEMPLATE = loader.get_template(settings.MARKDOWN_EDITOR_INIT_TEMPLATE)

    options = dict(
        previewParserPath=reverse('django_markdown_preview'),
        **settings.MARKDOWN_EDITOR_SETTINGS)
    options.update(extra_settings)
    ctx = dict(selector=selector, extra_settings=simplejson.dumps(options))
    return INIT_TEMPLATE.render(ctx)
