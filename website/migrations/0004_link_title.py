# Generated by Django 5.0 on 2023-12-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_link_linktype'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(default='Food Menu', max_length=200),
            preserve_default=False,
        ),
    ]
