# Generated by Django 5.0.3 on 2024-03-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='phone',
            field=models.CharField(default=485938888, max_length=10),
            preserve_default=False,
        ),
    ]
