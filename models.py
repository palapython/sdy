# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class Articles(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    creat_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('ArticlesCategory', models.DO_NOTHING, blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_top = models.IntegerField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey('Author', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'


class ArticlesCategory(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    creat_date = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles_category'


class ArticlesComements(models.Model):
    content = models.TextField(blank=True, null=True)
    creat_date = models.DateTimeField(blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    article = models.ForeignKey(Articles, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles_comements'


class ArticlesDetails(models.Model):
    content = models.TextField(blank=True, null=True)
    article = models.ForeignKey(Articles, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles_details'


class ArticlesPraise(models.Model):
    praise = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    articles = models.ForeignKey(Articles, models.DO_NOTHING, blank=True, null=True)
    creat_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles_praise'


class ArticlesTag(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    counts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles_tag'


class ArticlesToTag(models.Model):
    article = models.ForeignKey(Articles, models.DO_NOTHING, blank=True, null=True)
    tag = models.ForeignKey(ArticlesTag, models.DO_NOTHING, blank=True, null=True)
    creat_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles_to_tag'


class Author(models.Model):
    counts = models.IntegerField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author'


class Bxslider(models.Model):
    status = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    img = models.CharField(max_length=100, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bxslider'


class City(models.Model):
    city = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_session'


class Employees(models.Model):
    password = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    reg_time = models.DateTimeField(blank=True, null=True)
    last_time = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    qq = models.CharField(max_length=15, blank=True, null=True)
    wechat = models.CharField(max_length=30, blank=True, null=True)
    entry_time = models.DateTimeField(blank=True, null=True)
    birthday = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True)
    job_number = models.CharField(max_length=8, blank=True, null=True)
    last_ip = models.CharField(max_length=20, blank=True, null=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class MessagesSend(models.Model):
    m_status = models.IntegerField(db_column='m_Status', blank=True, null=True)  # Field name made lowercase.
    m_response_time = models.CharField(db_column='m_Response_Time', max_length=30, blank=True, null=True)  # Field name made lowercase.
    m_messageid = models.CharField(db_column='m_MessageID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    m_order_id = models.CharField(db_column='m_Order_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    m_text = models.CharField(db_column='m_Text', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    m_phone = models.CharField(db_column='m_Phone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    m_employee_id = models.IntegerField(db_column='m_Employee_ID', blank=True, null=True)  # Field name made lowercase.
    m_send_date = models.DateTimeField(db_column='m_Send_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'messages_send'


class MessagesVerifyCode(models.Model):
    m_status = models.IntegerField(db_column='m_Status', blank=True, null=True)  # Field name made lowercase.
    m_response_time = models.CharField(db_column='m_Response_Time', max_length=30, blank=True, null=True)  # Field name made lowercase.
    m_messageid = models.CharField(db_column='m_MessageID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    m_text = models.CharField(db_column='m_Text', max_length=300, blank=True, null=True)  # Field name made lowercase.
    m_phone = models.CharField(db_column='m_Phone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    m_send_date = models.DateTimeField(db_column='m_Send_Date', blank=True, null=True)  # Field name made lowercase.
    m_verifycode = models.IntegerField(db_column='m_verifyCode', blank=True, null=True)  # Field name made lowercase.
    m_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='m_User_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'messages_verify_code'


class OrderPayment(models.Model):
    p_status = models.IntegerField(db_column='p_Status', blank=True, null=True)  # Field name made lowercase.
    p_price = models.FloatField(db_column='p_Price', blank=True, null=True)  # Field name made lowercase.
    p_payment = models.IntegerField(db_column='p_Payment', blank=True, null=True)  # Field name made lowercase.
    p_sub_time = models.DateTimeField(db_column='p_Sub_Time', blank=True, null=True)  # Field name made lowercase.
    p_finish_time = models.DateTimeField(db_column='p_Finish_Time', blank=True, null=True)  # Field name made lowercase.
    p_u = models.ForeignKey('Users', models.DO_NOTHING, db_column='p_U_id', blank=True, null=True)  # Field name made lowercase.
    p_p = models.ForeignKey('Orders', models.DO_NOTHING, db_column='p_P_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_payment'


class Orders(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    order_code = models.CharField(max_length=16, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    cprice = models.FloatField(db_column='cPrice', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    coupon = models.FloatField(blank=True, null=True)
    voucher = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    order_state = models.CharField(max_length=24, blank=True, null=True)
    payment = models.CharField(max_length=20, blank=True, null=True)
    pay_number = models.IntegerField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    order_process = models.CharField(max_length=20, blank=True, null=True)
    remarik = models.CharField(max_length=600, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Process(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    process_name = models.CharField(max_length=30, blank=True, null=True)
    step_name = models.CharField(max_length=30, blank=True, null=True)
    employee_name = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    re_mark = models.CharField(max_length=500, blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'process'


class ProcessName(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    employee_name = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'process_name'


class ProcessStep(models.Model):
    process_name = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    p_name = models.ForeignKey(ProcessName, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'process_step'


class ProductCImage(models.Model):
    ul_name = models.CharField(db_column='ul_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ul_sourcename = models.CharField(db_column='ul_SourceName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ul_type = models.CharField(db_column='ul_Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ul_size = models.IntegerField(db_column='ul_Size', blank=True, null=True)  # Field name made lowercase.
    ul_posttime = models.DateTimeField(db_column='ul_PostTime', blank=True, null=True)  # Field name made lowercase.
    ul_employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='ul_Employee_id', blank=True, null=True)  # Field name made lowercase.
    ul_product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    ul_url = models.CharField(db_column='ul_Url', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_c_image'


class ProductCategory(models.Model):
    cate_name = models.CharField(db_column='cate_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cate_count = models.IntegerField(db_column='cate_Count', blank=True, null=True)  # Field name made lowercase.
    cate_date = models.DateTimeField(db_column='cate_Date', blank=True, null=True)  # Field name made lowercase.
    cate_employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='cate_Employee_id', blank=True, null=True)  # Field name made lowercase.
    cate_rootid = models.IntegerField(db_column='cate_RootID', blank=True, null=True)  # Field name made lowercase.
    cate_parentid = models.IntegerField(db_column='cate_ParentID', blank=True, null=True)  # Field name made lowercase.
    cate_sort = models.IntegerField(db_column='cate_Sort', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductService(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    renewal_reminder = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_service'


class ProductTImage(models.Model):
    ul_name = models.CharField(db_column='ul_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ul_sourcename = models.CharField(db_column='ul_SourceName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ul_type = models.CharField(db_column='ul_Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ul_size = models.IntegerField(db_column='ul_Size', blank=True, null=True)  # Field name made lowercase.
    ul_posttime = models.DateTimeField(db_column='ul_PostTime', blank=True, null=True)  # Field name made lowercase.
    ul_employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='ul_Employee_id', blank=True, null=True)  # Field name made lowercase.
    ul_url = models.CharField(db_column='ul_Url', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_t_image'


class Products(models.Model):
    p_name = models.CharField(db_column='p_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_price = models.FloatField(db_column='p_Price', blank=True, null=True)  # Field name made lowercase.
    p_market_price = models.FloatField(db_column='p_Market_Price', blank=True, null=True)  # Field name made lowercase.
    p_details = models.TextField(db_column='p_Details', blank=True, null=True)  # Field name made lowercase.
    p_putaway = models.IntegerField(db_column='p_Putaway', blank=True, null=True)  # Field name made lowercase.
    p_seo_title = models.CharField(db_column='p_Seo_Title', max_length=80, blank=True, null=True)  # Field name made lowercase.
    p_seo_keyword = models.CharField(db_column='p_Seo_Keyword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    p_seo_description = models.CharField(db_column='p_Seo_Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    p_entry_time = models.DateTimeField(db_column='p_Entry_Time', blank=True, null=True)  # Field name made lowercase.
    p_category = models.ForeignKey(ProductCategory, models.DO_NOTHING, db_column='p_Category_id', blank=True, null=True)  # Field name made lowercase.
    p_employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='p_Employee_id', blank=True, null=True)  # Field name made lowercase.
    p_top = models.IntegerField(db_column='p_Top', blank=True, null=True)  # Field name made lowercase.
    p_serivce = models.ForeignKey(ProductService, models.DO_NOTHING, db_column='p_Serivce_id', blank=True, null=True)  # Field name made lowercase.
    p_business = models.ForeignKey(ProcessName, models.DO_NOTHING, blank=True, null=True)
    p_image = models.ForeignKey(ProductTImage, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Roles(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    default = models.IntegerField(blank=True, null=True)
    permissions = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Users(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    qq = models.CharField(max_length=15, blank=True, null=True)
    wechat = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=30, blank=True, null=True)
    reg_time = models.DateTimeField(blank=True, null=True)
    last_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=300, blank=True, null=True)
    referrer = models.CharField(max_length=30, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    voucher = models.FloatField(blank=True, null=True)
    reg_employee = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.IntegerField(blank=True, null=True)
    know = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=30, blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    province = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'