# Generated by Django 4.1.7 on 2023-07-18 07:27

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_alter_pengajuan_gambar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rusak',
            fields=[
                ('rusakid', models.BigAutoField(primary_key=True, serialize=False)),
                ('tiperusak', models.CharField(choices=[('RUSAK BERAT', 'Kerusakan Berat'), ('RUSAK SEDANG', 'Kerusakan Sedang'), ('RUSAK RINGAN', 'Kerusakan Ringan')], default='RUSAK RINGAN', max_length=50)),
                ('deskrpsi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='kerusakan',
            old_name='deskrpsi',
            new_name='deskripsi',
        ),
        migrations.RenameField(
            model_name='kerusakan',
            old_name='rusakid',
            new_name='perencanaanid',
        ),
        migrations.RemoveField(
            model_name='beranda',
            name='nama_perencanaan',
        ),
        migrations.RemoveField(
            model_name='kerusakan',
            name='tiperusak',
        ),
        migrations.AddField(
            model_name='beranda',
            name='kerusakan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.kerusakan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kerusakan',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.demonslayer),
        ),
        migrations.AddField(
            model_name='kerusakan',
            name='jenis_perlengkapan',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='core.perlengkapan_jalan', to_field='jenis_perlengkapan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kerusakan',
            name='kondisi',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='core.kondisi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kerusakan',
            name='konstruksi_selesai',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='kerusakan',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.location'),
        ),
        migrations.AddField(
            model_name='kerusakan',
            name='nama_fasilitas',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='core.fasilitas_perlengkapan', to_field='nama_fasilitas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kerusakan',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.status'),
        ),
        migrations.AddField(
            model_name='kerusakan',
            name='tanggal_bangun',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='kerusakan',
            name='volume',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Perencanaan',
        ),
    ]
