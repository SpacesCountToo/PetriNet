# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objectify', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='x_val',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='y_val',
        ),
    ]
