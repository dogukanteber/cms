# Generated by Django 3.2.6 on 2021-08-12 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_userinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='tel_no',
            new_name='telephone_number',
        ),
    ]
