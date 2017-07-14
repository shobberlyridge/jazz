# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0013_lineup_date'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lineup',
            unique_together=set([('group_name', 'date')]),
        ),
    ]
