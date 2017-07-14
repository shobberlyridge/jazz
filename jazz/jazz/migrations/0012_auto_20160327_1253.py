# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0011_lineup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lineup',
            options={'verbose_name_plural': 'Lineups'},
        ),
    ]
