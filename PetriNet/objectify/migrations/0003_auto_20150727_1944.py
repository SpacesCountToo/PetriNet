# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objectify', '0002_auto_20150727_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='x_val',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='y_val',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
