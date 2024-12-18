# Generated by Django 5.0.6 on 2024-07-16 23:23

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfterSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_de', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Content De')),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Content En')),
            ],
            options={
                'verbose_name': 'After School',
                'verbose_name_plural': 'After Schools',
                'managed': True,
            },
        ),
    ]
