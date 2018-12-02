# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=15, verbose_name='\u7528\u6237\u540d')),
                ('user_passwd', models.CharField(max_length=40, verbose_name='\u5bc6\u7801')),
                ('user_level', models.CharField(default=b'0', max_length=2, verbose_name='\u7528\u6237\u6743\u9650\u7b49\u7ea7', choices=[(b'0', '\u666e\u901a\u7528\u6237'), (b'1', '\u540e\u53f0\u7ba1\u7406\u5458'), (b'2', '\u8d85\u7ea7\u7ba1\u7406\u5458')])),
            ],
            options={
                'db_table': 'userinfo',
                'verbose_name': '\u6ce8\u518c\u7528\u6237\u8868',
                'verbose_name_plural': '\u6ce8\u518c\u7528\u6237\u8868',
            },
        ),
    ]
