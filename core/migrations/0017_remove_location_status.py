# Generated by Django 4.1.7 on 2023-07-11 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_pengajuan_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='status',
        ),
    ]