# Generated by Django 4.0.5 on 2022-07-15 20:44

import core.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, max_length=20)),
                ('adult', models.BooleanField()),
                ('gender', models.CharField(choices=[('B', 'both'), ('M', 'male'), ('F', 'female')], default='B', max_length=5)),
                ('view_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SymptomQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', core.fields.IntegerRangeField()),
                ('question', models.TextField()),
                ('numberOfOption', core.fields.IntegerRangeField()),
                ('gender', models.CharField(choices=[('B', 'both'), ('M', 'male'), ('F', 'female')], default='B', max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='disease.symptom')),
            ],
        ),
        migrations.CreateModel(
            name='SymptomQuestionOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField()),
                ('value', models.IntegerField(default=1)),
                ('gender', models.CharField(choices=[('B', 'both'), ('M', 'male'), ('F', 'female')], default='B', max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='disease.symptomquestion')),
            ],
        ),
        migrations.CreateModel(
            name='SymptomFormula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_diagnose_id', models.JSONField()),
                ('sum', models.IntegerField()),
                ('result', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formulas', to='disease.symptom')),
            ],
        ),
    ]
