# Generated by Django 4.0.5 on 2022-07-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychology', '0014_delete_testuseranswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
    ]
