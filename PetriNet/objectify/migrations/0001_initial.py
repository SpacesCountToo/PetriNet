# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('uuid_name', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('human_readable_name', models.CharField(unique=True, max_length=50)),
                ('shape', models.CharField(max_length=1, choices=[(b'O', b'Form'), (b'L', b'Transform')])),
                ('x_val', models.IntegerField(null=True, blank=True)),
                ('y_val', models.IntegerField(null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='objectify.Unit', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='connection',
            name='destination',
            field=models.ForeignKey(related_name='dest', to='objectify.Unit'),
        ),
        migrations.AddField(
            model_name='connection',
            name='source',
            field=models.ForeignKey(related_name='src', to='objectify.Unit'),
        ),
    ]
