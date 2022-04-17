# Generated by Django 4.0.2 on 2022-04-13 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0021_scholarships_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarships',
            name='tag',
        ),
        migrations.AddField(
            model_name='scholarships',
            name='tag',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scholarship.tags'),
        ),
    ]
