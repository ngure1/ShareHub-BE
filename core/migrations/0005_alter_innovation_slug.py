# Generated by Django 5.0.4 on 2024-05-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_innovation_dataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovation',
            name='slug',
            field=models.SlugField(blank=True, default='djangodbmodelsfieldscharfield-djangodbmodelsfieldsdatetimefield', null=True, unique=True),
        ),
    ]