# Generated by Django 4.0.2 on 2022-02-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarships',
            name='post_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
