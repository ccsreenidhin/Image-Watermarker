# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 13:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orimage', models.ImageField(null=True, upload_to='original')),
                ('dupimage', models.ImageField(null=True, upload_to='wmarked')),
                ('text', models.CharField(max_length=200, null=True)),
                ('x', models.IntegerField(null=True)),
                ('y', models.IntegerField(null=True)),
                ('color', models.CharField(max_length=200, null=True)),
                ('fontsize', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galimage', models.ImageField(null=True, upload_to='galimage')),
            ],
        ),
    ]
