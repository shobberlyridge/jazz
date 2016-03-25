# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0009_auto_20150804_1208'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Band',
            new_name='Group',
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': 'Groups'},
        ),
        migrations.RenameField(
            model_name='group',
            old_name='band_name',
            new_name='group_name',
        ),
    ]
