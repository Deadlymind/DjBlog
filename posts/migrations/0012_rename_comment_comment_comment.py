# Generated by Django 4.2.7 on 2023-11-29 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment',
            new_name='comment',
        ),
    ]
