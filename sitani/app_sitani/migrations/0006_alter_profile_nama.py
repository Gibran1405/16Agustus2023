# Generated by Django 4.2.1 on 2023-07-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sitani', '0005_tokopertanian_nama_pemilik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Nama',
            field=models.CharField(max_length=100),
        ),
    ]
