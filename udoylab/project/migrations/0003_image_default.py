# Generated by Django 4.0.2 on 2022-04-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_imagealbum_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
