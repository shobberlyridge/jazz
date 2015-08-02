# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0003_people_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='sex',
            field=models.CharField(default=b'n', max_length=1, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'n', b'n/k')]),
            preserve_default=True,
        ),
    ]
