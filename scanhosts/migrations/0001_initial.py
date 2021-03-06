# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostLoginifo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=64, verbose_name='\u4e3b\u673aIP\u4fe1\u606f')),
                ('ssh_port', models.CharField(max_length=32, null=True, verbose_name='ssh\u767b\u5f55\u7684\u7aef\u53e3')),
                ('ssh_user', models.CharField(max_length=32, null=True, verbose_name='ssh\u767b\u5f55\u7684\u7528\u6237')),
                ('ssh_passwd', models.CharField(default=b'', max_length=64, null=True, verbose_name='ssh\u767b\u5f55\u7684\u7528\u6237')),
                ('ssh_rsa', models.CharField(default=b'', max_length=64, null=True, verbose_name='\u767b\u5f55\u4f7f\u7528\u7684\u79c1\u94a5')),
                ('rsa_pass', models.CharField(default=b'', max_length=64, null=True, verbose_name='\u79c1\u94a5\u7684\u79d8\u836f')),
                ('system_ver', models.CharField(default=b'', max_length=256, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c')),
                ('hostname', models.CharField(default=b'', max_length=256, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u4e3b\u673a\u540d')),
                ('ssh_status', models.IntegerField(default=0, verbose_name='0-\u767b\u5f55\u5931\u8d25,1-\u767b\u5f55\u6210\u529f')),
                ('ssh_type', models.IntegerField(default=0, verbose_name='1-rsa\u767b\u5f55,2-dsa\u767b\u5f55,3-\u666e\u901a\u7528\u6237rsa\u767b\u5f55,4-docker\u6210\u529f,5-docker\u65e0\u6cd5\u767b\u5f55')),
                ('mac_address', models.CharField(default=b'', max_length=512, verbose_name='mac\u5730\u5740\u5217\u8868')),
                ('sn', models.CharField(default=b'', max_length=256, verbose_name='SN\uff0d\u4e3b\u673a\u7684\u552f\u4e00\u6807\u793a')),
                ('mathine_type', models.CharField(default=b'', max_length=256, verbose_name='\u673a\u5668\u7684\u7c7b\u578b 1=\u7269\u7406\u670d\u52a1\u5668,2=\u865a\u62df\u8d44\u4ea7,3=\u7f51\u7edc\u8bbe\u5907 0=\u5176\u4ed6\u7c7b\u578b(\u672a\u77e5)')),
                ('sn_key', models.CharField(default=b'', max_length=256, verbose_name='\u552f\u4e00\u8bbe\u5907ID')),
                ('host_type', models.CharField(default=b'', max_length=256, null=True, verbose_name='\u865a\u62df\u673a\u4e0a\u5bbf\u4e3b\u673a\u7684\u7c7b\u578b')),
            ],
            options={
                'db_table': 'hostloginifo',
                'verbose_name': '\u521d\u59cb\u5316\u626b\u63cf\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u521d\u59cb\u5316\u626b\u63cf\u4fe1\u606f\u8868',
            },
        ),
    ]
