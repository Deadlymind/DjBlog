# Generated by Django 4.2.7 on 2023-11-08 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_publish_date2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish_date2',
        ),
    ]
