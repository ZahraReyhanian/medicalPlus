# Generated by Django 4.0.5 on 2022-07-15 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psychology', '0013_testuseranswer_updated_at_alter_test_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestUserAnswer',
        ),
    ]