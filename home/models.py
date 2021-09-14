from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock


class HomeExample(Page):
    template = 'home/home_example.html'
    max_count = 1


class HomePage(Page):
    template = 'home/home_page.html'
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=['bold', 'italic'], blank=False, null=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    blog_index = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    phone = models.CharField(max_length=20, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)

    content = StreamField([
        ('solid_three', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.CharBlock()),
            ('first', blocks.StructBlock([
                ('title', blocks.CharBlock()),
                ('description', blocks.CharBlock())
            ])),
            ('second', blocks.StructBlock([
                ('title', blocks.CharBlock()),
                ('description', blocks.CharBlock())
            ])),
            ('third', blocks.StructBlock([
                ('title', blocks.CharBlock()),
                ('description', blocks.CharBlock())
            ]))
        ], icon='list-ul')),
        ('image_four', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.CharBlock()),
            ('first', blocks.StructBlock([
                ('title', blocks.CharBlock()),
                ('description', blocks.CharBlock())
            ])),
            ('second', blocks.StructBlock([
                ('title', blocks.CharBlock()),
                ('description', blocks.CharBlock())
            ])),
            ('third', blocks.StructBlock([
                ('title', blocks.CharBlock()),
                ('description', blocks.CharBlock())
            ])),
            ('fourth', blocks.StructBlock([
                ('title', blocks.CharBlock()),
                ('description', blocks.CharBlock())
            ])),
            ('background', ImageChooserBlock()),
            ('image', ImageChooserBlock())
        ], icon='image')),
        ('portfolio_image', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.CharBlock()),
            ('tags', blocks.ListBlock(blocks.CharBlock(icon='tag'))),
            ('content', blocks.ListBlock(blocks.StructBlock([
                ('image', ImageChooserBlock(icon='image')),
                ('tag', blocks.ListBlock(blocks.CharBlock(icon='tag')))
            ], icon='image')))
        ], icon='image')),
        ('video_section', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.CharBlock()),
            ('link', blocks.URLBlock())
        ], icon='media')),
        ('three_with_button', blocks.StructBlock([
            ('title', blocks.CharBlock()),
            ('description', blocks.CharBlock()),
            ('cards', blocks.ListBlock(blocks.StructBlock([
                ('name', blocks.CharBlock()),
                ('price', blocks.CharBlock()),
                ('list', blocks.ListBlock(blocks.CharBlock(icon='list-ul'))),
                ('page', blocks.PageChooserBlock())
            ], icon='form')))
        ], icon='list-ul'))
    ], null=True, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        FieldPanel('phone'),
        FieldPanel('email'),
        ImageChooserPanel('banner_image'),
        PageChooserPanel('blog_index'),
        StreamFieldPanel('content')
    ]
