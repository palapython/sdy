# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'action',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('summary', models.CharField(blank=True, max_length=300, null=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('comments', models.IntegerField(blank=True, default=0, null=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(-1, '审核'), (0, '草稿'), (1, '公开')], null=True)),
                ('is_top', models.IntegerField(blank=True, null=True)),
                ('p_url', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='ArticlesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('sort', models.IntegerField(blank=True, null=True)),
                ('root_id', models.IntegerField(blank=True, default=0, null=True)),
                ('parent_id', models.IntegerField(blank=True, default=0, null=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'articles_category',
            },
        ),
        migrations.CreateModel(
            name='ArticlesComements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('root_id', models.IntegerField(blank=True, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Articles')),
            ],
            options={
                'db_table': 'articles_comements',
            },
        ),
        migrations.CreateModel(
            name='ArticlesDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('article', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Articles')),
            ],
            options={
                'db_table': 'articles_details',
            },
        ),
        migrations.CreateModel(
            name='ArticlesPraise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('praise', models.IntegerField(blank=True, null=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('articles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Articles')),
            ],
            options={
                'db_table': 'articles_praise',
            },
        ),
        migrations.CreateModel(
            name='ArticlesTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('counts', models.IntegerField(blank=True, default=0, null=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'articles_tag',
            },
        ),
        migrations.CreateModel(
            name='ArticlesToTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Articles')),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.ArticlesTag')),
            ],
            options={
                'db_table': 'articles_to_tag',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counts', models.IntegerField(blank=True, default=0, null=True)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Bxslider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, '下架'), (1, '上架')], default=1, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('img', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(max_length=100)),
                ('weight', models.IntegerField(blank=True, default=0, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bxslider',
            },
        ),
        migrations.CreateModel(
            name='Citys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('zipcode', models.IntegerField()),
            ],
            options={
                'db_table': 'china_city',
            },
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Citys')),
            ],
            options={
                'db_table': 'china_districts',
            },
        ),
        migrations.CreateModel(
            name='Employee2Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'employee2role',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=40, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('reg_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_time', models.DateTimeField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('qq', models.CharField(blank=True, max_length=15, null=True)),
                ('wechat', models.CharField(blank=True, max_length=30, null=True)),
                ('entry_time', models.DateTimeField(blank=True, null=True)),
                ('birthday', models.IntegerField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=30, null=True)),
                ('position', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=4, null=True)),
                ('job_number', models.CharField(blank=True, max_length=8, null=True)),
                ('last_ip', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='IndexNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('url', models.CharField(max_length=100)),
                ('status', models.BooleanField(choices=[(0, '下线'), (1, '上线')], default=1)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Employees')),
            ],
            options={
                'db_table': 'indexnavs',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
                ('weight', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_p', to='reposition.Menu')),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='MessagesSend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_status', models.IntegerField(blank=True, db_column='m_Status', null=True)),
                ('m_response_time', models.CharField(blank=True, db_column='m_Response_Time', max_length=30, null=True)),
                ('m_messageid', models.CharField(blank=True, db_column='m_MessageID', max_length=30, null=True)),
                ('m_order_id', models.CharField(blank=True, db_column='m_Order_ID', max_length=15, null=True)),
                ('m_text', models.CharField(blank=True, db_column='m_Text', max_length=2000, null=True)),
                ('m_phone', models.CharField(blank=True, db_column='m_Phone', max_length=11, null=True)),
                ('m_employee_id', models.IntegerField(blank=True, db_column='m_Employee_ID', null=True)),
                ('m_send_date', models.DateTimeField(auto_now_add=True, db_column='m_Send_Date', null=True)),
            ],
            options={
                'db_table': 'messages_send',
            },
        ),
        migrations.CreateModel(
            name='MessagesVerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_status', models.IntegerField(blank=True, db_column='m_Status', null=True)),
                ('m_response_time', models.CharField(blank=True, db_column='m_Response_Time', max_length=30, null=True)),
                ('m_messageid', models.CharField(blank=True, db_column='m_MessageID', max_length=30, null=True)),
                ('m_text', models.CharField(blank=True, db_column='m_Text', max_length=300, null=True)),
                ('m_phone', models.CharField(blank=True, db_column='m_Phone', max_length=11, null=True)),
                ('m_send_date', models.DateTimeField(auto_now_add=True, db_column='m_Send_Date', null=True)),
                ('m_verifycode', models.IntegerField(blank=True, db_column='m_verifyCode', null=True)),
            ],
            options={
                'db_table': 'messages_verify_code',
            },
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_status', models.IntegerField(blank=True, db_column='p_Status', null=True)),
                ('p_price', models.FloatField(blank=True, db_column='p_Price', null=True)),
                ('p_payment', models.IntegerField(blank=True, db_column='p_Payment', null=True)),
                ('p_sub_time', models.DateTimeField(auto_now_add=True, db_column='p_Sub_Time', null=True)),
                ('p_finish_time', models.DateTimeField(blank=True, db_column='p_Finish_Time', null=True)),
            ],
            options={
                'db_table': 'order_payment',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('order_code', models.CharField(blank=True, max_length=16, null=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('cprice', models.FloatField(blank=True, db_column='cPrice', null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('coupon', models.FloatField(blank=True, default=0, null=True)),
                ('voucher', models.FloatField(blank=True, default=0, null=True)),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('order_state', models.CharField(choices=[(0, '待付款'), (1, '待服务'), (2, '服务中'), (3, '服务完成')], default=0, max_length=24)),
                ('payment', models.CharField(choices=[(0, '支付宝'), (1, '微信'), (2, '线下支付'), (3, '网银支付')], max_length=20, null=True)),
                ('pay_number', models.IntegerField(blank=True, null=True)),
                ('pay_time', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('order_process', models.CharField(blank=True, max_length=20, null=True)),
                ('remark', models.CharField(blank=True, max_length=600, null=True)),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('province', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('area', models.CharField(blank=True, max_length=20, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=32)),
                ('weight', models.IntegerField(default=0)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reposition.Menu')),
            ],
            options={
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='Permission2Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Action')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Permission')),
            ],
            options={
                'db_table': 'permission2action',
            },
        ),
        migrations.CreateModel(
            name='Permission2Action2Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p2a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Permission2Action')),
            ],
            options={
                'db_table': 'permission2action2role',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(blank=True, null=True)),
                ('process_name', models.CharField(blank=True, max_length=30, null=True)),
                ('step_name', models.CharField(blank=True, max_length=30, null=True)),
                ('employee_name', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('re_mark', models.CharField(blank=True, max_length=500, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees')),
            ],
            options={
                'db_table': 'process',
            },
        ),
        migrations.CreateModel(
            name='ProcessName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('employee_name', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modify_time', models.DateTimeField(blank=True, null=True)),
                ('state', models.IntegerField(blank=True, default=1, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees')),
            ],
            options={
                'db_table': 'process_name',
            },
        ),
        migrations.CreateModel(
            name='ProcessStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_name', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('employee_name', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modify_time', models.DateTimeField(blank=True, null=True)),
                ('state', models.IntegerField(blank=True, default=1, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees')),
                ('p_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.ProcessName')),
            ],
            options={
                'db_table': 'process_step',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_name', models.CharField(blank=True, db_column='cate_Name', max_length=10, null=True)),
                ('cate_count', models.IntegerField(blank=True, db_column='cate_Count', default=0, null=True)),
                ('cate_date', models.DateTimeField(auto_now_add=True, db_column='cate_Date', null=True)),
                ('cate_rootid', models.IntegerField(blank=True, db_column='cate_RootID', default=0, null=True)),
                ('cate_parentid', models.IntegerField(blank=True, db_column='cate_ParentID', default=0, null=True)),
                ('cate_sort', models.IntegerField(blank=True, db_column='cate_Sort', null=True)),
                ('cate_employee', models.ForeignKey(blank=True, db_column='cate_Employee_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees')),
            ],
            options={
                'db_table': 'product_category',
            },
        ),
        migrations.CreateModel(
            name='ProductCImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ul_name', models.CharField(blank=True, db_column='ul_Name', max_length=100, null=True)),
                ('ul_sourcename', models.CharField(blank=True, db_column='ul_SourceName', max_length=30, null=True)),
                ('ul_type', models.CharField(blank=True, db_column='ul_Type', max_length=10, null=True)),
                ('ul_size', models.IntegerField(blank=True, db_column='ul_Size', null=True)),
                ('ul_posttime', models.DateTimeField(auto_now_add=True, db_column='ul_PostTime', null=True)),
                ('ul_url', models.CharField(blank=True, db_column='ul_Url', max_length=100, null=True)),
                ('ul_employee', models.ForeignKey(blank=True, db_column='ul_Employee_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees')),
            ],
            options={
                'db_table': 'product_c_image',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(blank=True, db_column='p_Name', max_length=50, null=True)),
                ('p_price', models.FloatField(blank=True, db_column='p_Price', null=True)),
                ('p_market_price', models.FloatField(blank=True, db_column='p_Market_Price', null=True)),
                ('p_details', models.TextField(blank=True, db_column='p_Details', null=True)),
                ('p_putaway', models.IntegerField(blank=True, choices=[(0, '下线'), (1, '上线')], db_column='p_Putaway', default=1, null=True)),
                ('p_seo_title', models.CharField(blank=True, db_column='p_Seo_Title', max_length=80, null=True)),
                ('p_seo_keyword', models.CharField(blank=True, db_column='p_Seo_Keyword', max_length=100, null=True)),
                ('p_seo_description', models.CharField(blank=True, db_column='p_Seo_Description', max_length=200, null=True)),
                ('p_ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('p_top', models.IntegerField(blank=True, db_column='p_Top', default=0, null=True)),
                ('p_business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.ProcessName')),
                ('p_category', models.ForeignKey(blank=True, db_column='p_Category_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.ProductCategory')),
                ('p_employee', models.ForeignKey(blank=True, db_column='p_Employee_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('renewal_reminder', models.IntegerField(blank=True, choices=[(0, '不提醒'), (1, '提醒')], null=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.ProductCategory')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees')),
            ],
            options={
                'db_table': 'product_service',
            },
        ),
        migrations.CreateModel(
            name='ProductTImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ul_name', models.CharField(blank=True, db_column='ul_Name', max_length=50, null=True)),
                ('ul_sourcename', models.CharField(blank=True, db_column='ul_SourceName', max_length=30, null=True)),
                ('ul_type', models.CharField(blank=True, db_column='ul_Type', max_length=10, null=True)),
                ('ul_size', models.IntegerField(blank=True, db_column='ul_Size', null=True)),
                ('ul_posttime', models.DateTimeField(auto_now_add=True, db_column='ul_PostTime', null=True)),
                ('ul_url', models.CharField(blank=True, db_column='ul_Url', max_length=100, null=True)),
                ('ul_employee', models.ForeignKey(blank=True, db_column='ul_Employee_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees')),
                ('ul_product', models.ForeignKey(blank=True, db_column='ul_Product_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pro_image', to='reposition.Products')),
            ],
            options={
                'db_table': 'product_t_image',
            },
        ),
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'china_provinces',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=30)),
                ('qq', models.CharField(max_length=15, null=True)),
                ('wechat', models.CharField(blank=True, max_length=30, null=True)),
                ('group', models.CharField(blank=True, max_length=30, null=True)),
                ('reg_time', models.DateTimeField(auto_now_add=True)),
                ('last_time', models.DateTimeField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=300, null=True)),
                ('referrer', models.CharField(blank=True, max_length=30, null=True)),
                ('balance', models.FloatField(blank=True, null=True)),
                ('voucher', models.FloatField(blank=True, null=True)),
                ('province', models.IntegerField(blank=True, default=0, null=True)),
                ('city', models.IntegerField(blank=True, default=0, null=True)),
                ('area', models.IntegerField(blank=True, default=0, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=30, null=True)),
                ('know', models.IntegerField(blank=True, default=0, null=True)),
                ('reg_employee', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='p_service',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.ProductService'),
        ),
        migrations.AddField(
            model_name='productcimage',
            name='ul_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Products'),
        ),
        migrations.AddField(
            model_name='permission2action2role',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Role'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Users'),
        ),
        migrations.AddField(
            model_name='orderpayment',
            name='p_p',
            field=models.ForeignKey(blank=True, db_column='p_P_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Orders'),
        ),
        migrations.AddField(
            model_name='orderpayment',
            name='p_u',
            field=models.ForeignKey(blank=True, db_column='p_U_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Users'),
        ),
        migrations.AddField(
            model_name='messagesverifycode',
            name='m_user',
            field=models.ForeignKey(blank=True, db_column='m_User_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Users'),
        ),
        migrations.AddField(
            model_name='employees',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Role'),
        ),
        migrations.AddField(
            model_name='employee2role',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Employees'),
        ),
        migrations.AddField(
            model_name='employee2role',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Role'),
        ),
        migrations.AddField(
            model_name='citys',
            name='p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reposition.Provinces'),
        ),
        migrations.AddField(
            model_name='bxslider',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees'),
        ),
        migrations.AddField(
            model_name='author',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Employees'),
        ),
        migrations.AddField(
            model_name='articlestag',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Author'),
        ),
        migrations.AddField(
            model_name='articlespraise',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Users'),
        ),
        migrations.AddField(
            model_name='articlescomements',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Users'),
        ),
        migrations.AddField(
            model_name='articlescategory',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Author'),
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.Author'),
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reposition.ArticlesCategory'),
        ),
    ]
