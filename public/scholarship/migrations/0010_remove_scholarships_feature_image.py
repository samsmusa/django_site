# Generated by Django 4.0.2 on 2022-02-15 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0009_alter_scholarships_feature_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarships',
            name='feature_image',
        ),
    ]
