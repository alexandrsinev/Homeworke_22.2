# Generated by Django 5.0.4 on 2024-05-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.IntegerField(verbose_name='номер версии'),
        ),
    ]
