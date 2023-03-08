# Generated by Django 4.1.2 on 2023-02-11 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_plant_attracts_pollinators_plant_blooming_fruiting_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plants.category'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plants.subcategory'),
        ),
    ]
