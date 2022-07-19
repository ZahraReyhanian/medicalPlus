# Generated by Django 4.0.5 on 2022-07-17 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0002_alter_symptom_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptomformula',
            name='option_diagnose_id',
        ),
        migrations.CreateModel(
            name='SymptomFormulaOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='disease.symptom')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disease.symptomquestionoption')),
            ],
        ),
    ]
