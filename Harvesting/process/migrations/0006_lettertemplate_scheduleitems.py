# Generated by Django 4.1.2 on 2023-07-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0005_lettertorm'),
    ]

    operations = [
        migrations.CreateModel(
            name='LetterTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('template_id', models.CharField(max_length=200, unique=True)),
                ('template_text', models.CharField(blank=True, default=None, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleItems',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_text', models.CharField(blank=True, default=None, max_length=10000, null=True)),
                ('item_order', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('item_enabled', models.BooleanField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
    ]
