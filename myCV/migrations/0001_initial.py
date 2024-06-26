# Generated by Django 5.0.2 on 2024-05-05 10:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of the setting.', max_length=254, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='Description')),
                ('parameter', models.CharField(blank=True, default='', max_length=254, verbose_name='Parameter')),
            ],
            options={
                'verbose_name': 'General Setting',
                'verbose_name_plural': 'General Settings',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ImageSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of the setting.', max_length=254, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='Description')),
                ('file', models.ImageField(blank=True, default='', upload_to='images', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Image Setting',
                'verbose_name_plural': 'Image Settings',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of the setting.', max_length=254, verbose_name='Name')),
                ('percentage', models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percentage')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('link', models.URLField(blank=True, default='', max_length=254, verbose_name='Link')),
                ('icon', models.CharField(blank=True, default='', max_length=254, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Media',
                'ordering': ('order',),
            },
        ),
    ]
