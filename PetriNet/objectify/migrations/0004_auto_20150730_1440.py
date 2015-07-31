# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objectify', '0003_auto_20150727_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='destination',
            field=models.ForeignKey(related_name='src', to='objectify.Unit'),
        ),
        migrations.AlterField(
            model_name='connection',
            name='source',
            field=models.ForeignKey(related_name='dest', to='objectify.Unit'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='x_val',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='y_val',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
