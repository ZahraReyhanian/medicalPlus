# Generated by Django 4.0.5 on 2022-07-03 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychology', '0005_rename_description_test_body_alter_test_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
