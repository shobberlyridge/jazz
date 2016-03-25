# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0002_auto_20150728_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
