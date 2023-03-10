# Generated by Django 4.1.2 on 2023-02-20 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_plant_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='plant',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='plant',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='plant',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
