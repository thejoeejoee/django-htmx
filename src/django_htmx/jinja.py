from __future__ import annotations

from django.conf import settings
from django.templatetags.static import static
from django.utils.html import format_html


def django_htmx_script() -> str:
    # Optimization: whilst the script has no behaviour outside of debug mode,
    # don't include it. Same if exception propagating is enabled in Django.
    if not settings.DEBUG or settings.DEBUG_PROPAGATE_EXCEPTIONS:
        return format_html("")
    return format_html(
        '<script type="text/javascript" src="{}" data-debug="{}" defer></script>',
        static("django-htmx.js"),
        str(bool(settings.DEBUG)),
    )
