# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wagtail.wagtailcore.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0010_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='website',
        ),
        migrations.RemoveField(
            model_name='source',
            name='website',
        ),
        migrations.AddField(
            model_name='event',
            name='event_text',
            field=wagtail.wagtailcore.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
