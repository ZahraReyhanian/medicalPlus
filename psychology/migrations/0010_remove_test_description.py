# Generated by Django 4.0.5 on 2022-07-13 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psychology', '0009_alter_test_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='description',
        ),
    ]