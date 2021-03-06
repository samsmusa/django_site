# Generated by Django 4.0.2 on 2022-02-14 12:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0003_alter_scholarships_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['is_read', 'created'],
            },
        ),
        migrations.AlterModelOptions(
            name='scholarships',
            options={'ordering': ['-add_date']},
        ),
    ]
