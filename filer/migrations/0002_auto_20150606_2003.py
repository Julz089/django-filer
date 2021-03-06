# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='polymorphic_ctype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='polymorphic_filer.file_set+', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
    ]
