# Generated by Django 4.1.5 on 2023-04-01 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jokes',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
