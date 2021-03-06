# Generated by Django 3.2.6 on 2021-09-10 15:39

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_homepage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('solid_three', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock()), ('first', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock())])), ('second', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock())])), ('third', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock())]))], icon='list-ul')), ('image_four', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock()), ('first', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock())])), ('second', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock())])), ('third', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock())])), ('fourth', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock())])), ('background', wagtail.images.blocks.ImageChooserBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], icon='image')), ('portfolio_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock()), ('tags', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(icon='tag'))), ('content', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('tag', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(icon='tag')))], icon='image')))], icon='image')), ('video_section', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock())], icon='media')), ('three_with_button', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock()), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('price', wagtail.core.blocks.CharBlock()), ('list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(icon='list-ul'))), ('page', wagtail.core.blocks.PageChooserBlock())], icon='form')))], icon='list-ul'))], null=True),
        ),
    ]
