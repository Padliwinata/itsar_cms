# Generated by Django 3.2.6 on 2021-09-09 03:20

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210908_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='featured',
            field=wagtail.core.fields.StreamField([('page', wagtail.core.blocks.PageChooserBlock())], blank=True),
        ),
    ]
