# Generated by Django 4.2.1 on 2023-07-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sitani', '0002_tokopertanian_deskripsi'),
    ]

    operations = [
        migrations.AddField(
            model_name='beritapertanian',
            name='Penulis',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
