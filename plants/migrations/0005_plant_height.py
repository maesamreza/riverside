# Generated by Django 4.1.2 on 2023-02-12 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_alter_tip_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='height',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
