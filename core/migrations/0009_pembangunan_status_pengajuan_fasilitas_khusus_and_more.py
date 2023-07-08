# Generated by Django 4.1.7 on 2023-07-07 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_pembangunan_gambar_alter_pengajuan_gambar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembangunan',
            name='status',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pengajuan',
            name='Fasilitas_khusus',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='pengajuan',
            name='statuspengajuan',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.status'),
        ),
        migrations.AlterField(
            model_name='penyeleksian',
            name='status',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.status'),
        ),
        migrations.AlterField(
            model_name='perencanaan',
            name='status_pengajuan',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.status'),
        ),
    ]
