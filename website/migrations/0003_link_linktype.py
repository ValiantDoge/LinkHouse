# Generated by Django 5.0 on 2023-12-17 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='linktype',
            field=models.CharField(choices=[('1', 'Food'), ('2', 'Drinks/Bar')], default='1', max_length=100),
        ),
    ]
