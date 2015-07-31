# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objectify', '0004_auto_20150730_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='x_val',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='y_val',
            field=models.IntegerField(default=0),
        ),
    ]
