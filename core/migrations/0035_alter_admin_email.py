# Generated by Django 4.1.7 on 2023-07-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_admin_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email Admin'),
        ),
    ]