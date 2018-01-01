# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reposition', '0029_auto_20170709_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsPackages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('description', models.TextField(verbose_name='描述')),
            ],
            options={
                'db_table': 'products_packages',
                'verbose_name': '产品套餐表',
                'verbose_name_plural': '产品套餐表',
            },
        ),
        migrations.CreateModel(
            name='ProductsPackages2P',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('pp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.ProductsPackages')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Products')),
            ],
            options={
                'db_table': 'products_packages2p',
                'verbose_name': '产品套餐对应的商品',
                'verbose_name_plural': '产品套餐对应的商品',
            },
        ),
    ]
