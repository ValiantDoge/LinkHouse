# Generated by Django 4.2.3 on 2024-01-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='desc',
            field=models.TextField(default='Explore Our Menu!'),
            preserve_default=False,
        ),
    ]
