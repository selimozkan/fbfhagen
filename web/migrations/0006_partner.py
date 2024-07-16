# Generated by Django 5.0.6 on 2024-07-15 23:30

import django.core.validators
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_project_description_en'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, null=True, quality=100, scale=None, size=[233, 50], upload_to='partner/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'png', 'jpg'])], verbose_name='Image')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'managed': True,
            },
        ),
    ]
