# Generated by Django 3.2.6 on 2021-08-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.JSONField(verbose_name={1: 'null'}),
        ),
    ]