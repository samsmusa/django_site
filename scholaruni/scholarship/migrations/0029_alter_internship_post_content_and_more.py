# Generated by Django 4.0.2 on 2022-05-11 10:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0028_updatedschol_rename_updated_updatedintern'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='post_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='post_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]