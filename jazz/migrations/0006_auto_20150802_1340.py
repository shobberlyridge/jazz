# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0005_instrument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrument',
            name='instrument',
        ),
        migrations.DeleteModel(
            name='Instrument',
        ),
    ]
