# Generated by Django 4.0.5 on 2022-07-31 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'not started'), ('2', 'failed'), ('3', 'error'), ('4', 'blocked'), ('5', 'returned to payer'), ('6', 'systemic returned'), ('7', 'canceled'), ('8', 'tranfered to gateway'), ('10', 'waiting to accept'), ('100', 'confirmed')], default='1', max_length=5)),
                ('track_id', models.CharField(max_length=100, null=True)),
                ('refID', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(max_length=200, null=True)),
                ('amount', models.CharField(max_length=255)),
                ('object_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
