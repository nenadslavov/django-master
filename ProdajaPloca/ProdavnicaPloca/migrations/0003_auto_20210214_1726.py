# Generated by Django 3.0.11 on 2021-02-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProdavnicaPloca', '0002_auto_20210214_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ploca',
            name='album',
            field=models.CharField(db_index=True, default='album', max_length=200),
        ),
        migrations.AlterField(
            model_name='ploca',
            name='cena',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]