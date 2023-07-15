# Generated by Django 4.1.7 on 2023-07-13 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_pembangunan_jenis_perlengkapan_pembangunan_kondisi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kerusakan',
            fields=[
                ('rusakid', models.BigAutoField(primary_key=True, serialize=False)),
                ('tiperusak', models.CharField(choices=[('RUSAK BERAT', 'Kerusakan Berat'), ('RUSAK SEDANG', 'Kerusakan Sedang'), ('RUSAK RINGAN', 'Kerusakan Ringan')], default='RUSAK RINGAN', max_length=50)),
                ('deskrpsi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kondisi',
            fields=[
                ('Kondisiid', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipekondisi', models.CharField(choices=[('BAIK', 'Kondisi Baik'), ('BURUK', 'Kondisi Buruk')], default='BAIK', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='fasilitas_perlengkapan',
            name='kondisi',
        ),
        migrations.RemoveField(
            model_name='perencanaan',
            name='fasilitasid',
        ),
        migrations.RemoveField(
            model_name='perencanaan',
            name='pembangunanid',
        ),
        migrations.AddField(
            model_name='perencanaan',
            name='jenis_perlengkapan',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='core.perlengkapan_jalan', to_field='jenis_perlengkapan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perencanaan',
            name='nama_fasilitas',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='core.fasilitas_perlengkapan', to_field='nama_fasilitas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pembangunan',
            name='kondisi',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.kondisi'),
        ),
    ]