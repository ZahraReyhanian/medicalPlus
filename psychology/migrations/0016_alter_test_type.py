# Generated by Django 4.0.5 on 2022-07-31 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychology', '0015_alter_test_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='type',
            field=models.CharField(choices=[('free', 'free'), ('cash', 'cash')], max_length=5),
        ),
    ]
