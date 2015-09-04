from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class TeamMemberPage(Page):
    """
    Place holder for wagtail_blog app.
    """
    name = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
    ]
