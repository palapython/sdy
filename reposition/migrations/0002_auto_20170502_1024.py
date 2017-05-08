# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reposition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='p_business',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reposition.ProcessStep'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mytask',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='分配时间'),
        ),
        migrations.AlterField(
            model_name='mytask',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Orders', verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='orderserice',
            name='allocation_status',
            field=models.SmallIntegerField(choices=[(0, '未分配'), (1, '已分配')], default=False, verbose_name='分配状态'),
        ),
    ]
