# Generated by Django 4.2.3 on 2024-01-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_link_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
