# Generated by Django 2.2.1 on 2019-05-19 20:39

import ckeditor_uploader.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190519_0529'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchievedObjectiveQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(default='NA', max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('state', models.CharField(choices=[('created', 'created'), ('imported', 'imported'), ('processed', 'processed'), ('duplicate', 'duplicate'), ('rejected', 'rejected'), ('approved', 'approved')], default=('created', 'created'), max_length=100)),
                ('level', models.IntegerField(default=0)),
                ('length', models.CharField(default='', max_length=25)),
                ('question_html', ckeditor_uploader.fields.RichTextUploadingField()),
                ('solution_html', ckeditor_uploader.fields.RichTextUploadingField()),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=ckeditor_uploader.fields.RichTextUploadingField(), blank=True, null=True, size=None)),
                ('correct_option', models.CharField(default='', max_length=500, null=True)),
                ('inquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.InQuestion')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='ArchievedSubjectiveQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(default='NA', max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('state', models.CharField(choices=[('created', 'created'), ('imported', 'imported'), ('processed', 'processed'), ('duplicate', 'duplicate'), ('rejected', 'rejected'), ('approved', 'approved')], default=('created', 'created'), max_length=100)),
                ('level', models.IntegerField(default=0)),
                ('length', models.CharField(default='', max_length=25)),
                ('question_html', ckeditor_uploader.fields.RichTextUploadingField()),
                ('solution_html', ckeditor_uploader.fields.RichTextUploadingField()),
                ('inquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.InQuestion')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Topic')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='state',
            field=models.CharField(choices=[('created', 'created'), ('imported', 'imported'), ('processed', 'processed'), ('duplicate', 'duplicate'), ('rejected', 'rejected'), ('approved', 'approved')], default=('created', 'created'), max_length=100),
        ),
        migrations.DeleteModel(
            name='ArchievedQuestion',
        ),
    ]