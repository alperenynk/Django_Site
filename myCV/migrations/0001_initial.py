# Generated by Django 5.0.2 on 2024-04-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=254)),
                ('description', models.CharField(blank=True, default='', max_length=254)),
                ('parameter', models.CharField(blank=True, default='', max_length=254)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]