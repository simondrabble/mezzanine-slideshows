from django.db import models

from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
from mezzanine.pages.models import RichTextPage
from mezzanine.galleries.models import Gallery


class SlideshowManager(models.Manager):

    def published(self):
        return self.filter(gallery__status=CONTENT_STATUS_PUBLISHED)


class Slideshow(models.Model):
    objects = SlideshowManager()

    page = models.OneToOneField(RichTextPage)
    gallery = models.ForeignKey(Gallery)
    slideshow_title = models.CharField(max_length=30, blank=True,
                                       help_text="A brief description of the slideshow")
    slideshow_description = models.TextField(max_length=100, blank=True,
                                             help_text="A fuller description of the slideshow")

    # These fields have the same meaning as at
    # http://www.owlgraphic.com/owlcarousel/index.html#customizing
    slide_speed = models.IntegerField(
            default=500, null=False, blank=False,
            help_text="When autoplaying, display with this delay (ms) between slides")
    pagination_speed = models.IntegerField(
            default=1200, null=False, blank=False,
            help_text="Pagination speed")
    autoplay = models.BooleanField(default=True,
                                   help_text="Autoplay slideshow")
    mousedrag = models.BooleanField(default=False,
                                    help_text="Allow mouse dragging")
    pagination = models.BooleanField(default=False,
                                     help_text="Show pagination")
    navigation = models.BooleanField(default=True,
                                     help_text="Show navigation")
    scroll_per_page = models.BooleanField(default=False,
                                          help_text="Scroll per page (not per item)")
    items = models.SmallIntegerField(default=3,
                                     blank=False,
                                     null=False,
                                     help_text="Display this many items at a time")
    lazy_load = models.BooleanField(default=False,
                                    help_text="Lazy load images")

    class Meta:
        verbose_name = "Slideshow"
        verbose_name_plural = "Slideshows"

    def __str__(self):
        return self.page.title
