# Generated by Django 4.0.5 on 2022-07-17 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0003_remove_symptomformula_option_diagnose_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptomformulaoption',
            name='formula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='disease.symptomformula'),
        ),
    ]
