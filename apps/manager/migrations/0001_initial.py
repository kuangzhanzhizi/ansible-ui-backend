# Generated by Django 2.2.16 on 2021-08-29 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import vadmin.op_drf.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('group_name', models.CharField(max_length=80, null=True, verbose_name='主机组')),
                ('nick_name', models.CharField(max_length=80, unique=True, verbose_name='别名')),
                ('_status', models.IntegerField(choices=[(0, '禁用中'), (1, '使用中'), (2, '暂停中'), (3, '不可达')], default=0)),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '主机列表',
                'verbose_name_plural': '主机列表',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', vadmin.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', vadmin.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', vadmin.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', vadmin.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('host_name', models.CharField(max_length=80, null=True, verbose_name='主机名称')),
                ('conn_ip', models.CharField(max_length=80, unique=True, verbose_name='主机IP')),
                ('ansible_user', models.CharField(default='root', max_length=80, verbose_name='主机用户')),
                ('ansible_pwd', models.CharField(blank=True, max_length=80, null=True, verbose_name='密码')),
                ('ssh_key', models.CharField(default='files/id_rsa', max_length=80, null=True, verbose_name='ssh私匙')),
                ('sys_name', models.CharField(default='Linux', max_length=80, null=True, verbose_name='系统名称')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('groups', models.ManyToManyField(blank=True, related_name='hosts', to='manager.Group', verbose_name='主机组')),
            ],
            options={
                'verbose_name': '主机列表',
                'verbose_name_plural': '主机列表',
            },
        ),
    ]
