# Generated by Django 4.0.2 on 2022-02-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0002_scholarships_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarships',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
