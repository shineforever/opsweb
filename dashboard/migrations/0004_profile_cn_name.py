# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170827_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cn_name',
            field=models.CharField(max_length=20, null=True, verbose_name='\u4e2d\u6587\u540d'),
        ),
    ]
