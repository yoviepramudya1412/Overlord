# Generated by Django 4.1.7 on 2023-07-15 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_remove_perencanaan_nama_perencanaan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fasilitas_perlengkapan',
            name='tanggal_ditambahkan',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fasilitas_perlengkapan',
            name='tipekhusus',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
