# Generated by Django 4.0.5 on 2022-06-13 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('questions', models.IntegerField()),
                ('type', models.CharField(choices=[('free', 'free'), ('cash', 'cash'), ('vip', 'vip')], max_length=5)),
                ('price', models.CharField(max_length=255)),
                ('answers', models.TextField(null=True)),
                ('image', models.TextField(null=True)),
                ('tags', models.CharField(max_length=255)),
                ('viewCount', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('question', models.TextField()),
                ('numberOfAnswer', models.PositiveIntegerField()),
                ('answers', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testquestions', to='psychology.test')),
            ],
        ),
        migrations.CreateModel(
            name='TestUserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('N', 'not started'), ('G', 'get strated'), ('S', 'submitted')], default='N', max_length=5)),
                ('result', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_status', to='psychology.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestUserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_choice', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='psychology.testquestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField()),
                ('grade', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testresults', to='psychology.test')),
            ],
        ),
    ]
