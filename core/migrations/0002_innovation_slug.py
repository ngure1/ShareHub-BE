# Generated by Django 5.0.4 on 2024-05-03 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovation',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
