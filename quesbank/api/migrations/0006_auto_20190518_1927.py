# Generated by Django 2.2.1 on 2019-05-18 13:57

import ckeditor_uploader.fields
import django.contrib.postgres.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190518_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectivequestion',
            name='options',
            field=django.contrib.postgres.fields.ArrayField(base_field=ckeditor_uploader.fields.RichTextUploadingField(), blank=True, null=True, size=None),
        ),
    ]