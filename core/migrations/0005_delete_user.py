# Generated by Django 4.1.7 on 2023-06-24 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_user_is_user_remove_user_nama_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
