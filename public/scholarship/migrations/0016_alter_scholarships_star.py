# Generated by Django 4.0.2 on 2022-02-21 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0015_scholarships_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarships',
            name='star',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
