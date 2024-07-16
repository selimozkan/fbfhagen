# Generated by Django 5.0.6 on 2024-07-16 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_footercontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, max_length=250, null=True, verbose_name='Facebook Link')),
                ('instagram', models.URLField(blank=True, max_length=250, null=True, verbose_name='Instagram Link')),
                ('youtube', models.URLField(blank=True, max_length=250, null=True, verbose_name='Youtube Link')),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='footercontact',
            options={'managed': True, 'verbose_name': 'Footer Contact', 'verbose_name_plural': 'Footer Contacts'},
        ),
    ]
