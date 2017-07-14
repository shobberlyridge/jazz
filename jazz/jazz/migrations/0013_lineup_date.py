# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0012_auto_20160327_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineup',
            name='date',
            field=models.DateField(null=True, verbose_name=b'Date', blank=True),
            preserve_default=True,
        ),
    ]
