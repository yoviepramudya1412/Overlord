# Generated by Django 4.1.7 on 2023-08-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_pengajuan_tanggal_ajukan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengajuan',
            name='tanggal_ajukan',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
