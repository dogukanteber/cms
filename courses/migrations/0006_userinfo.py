# Generated by Django 3.2.6 on 2021-08-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel_no', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=512)),
                ('profession', models.CharField(max_length=64)),
            ],
        ),
    ]
