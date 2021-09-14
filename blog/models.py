from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, RichTextField, FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


# Create your models here.
class BlogIndexPage(Page):
    max_count = 1
    featured = StreamField([
        ('page', blocks.PageChooserBlock())
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('featured')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        context['user'] = request.user
        return context


class BlogPage(Page):
    template = 'blog/blog_page.html'

    description = RichTextField(blank=False, null=True)
    author = models.CharField(max_length=100, blank=False, null=True)

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('quote', blocks.RichTextBlock())
    ], blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('author')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('author'),
        ImageChooserPanel('banner_image'),
        StreamFieldPanel('content')
    ]

