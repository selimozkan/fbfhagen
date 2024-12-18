# Generated by Django 5.0.6 on 2024-07-15 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_partner_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Address')),
                ('email', models.CharField(blank=True, max_length=250, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Phone')),
                ('instagram', models.URLField(blank=True, max_length=250, null=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Footer Contact',
                'verbose_name_plural': 'footer Contacts',
                'managed': True,
            },
        ),
    ]
