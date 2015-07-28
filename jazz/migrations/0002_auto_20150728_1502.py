# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='people',
            name='first_name',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
