# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jazz', '0010_auto_20150804_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lineup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.ForeignKey(to='jazz.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
