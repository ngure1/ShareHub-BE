# Generated by Django 5.0.4 on 2024-05-10 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_updated',
            field=models.BooleanField(default=False, verbose_name='Is updated'),
            preserve_default=False,
        ),
    ]
