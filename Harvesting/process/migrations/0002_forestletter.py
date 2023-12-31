# Generated by Django 4.1.2 on 2023-07-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForestLetter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('system_no', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('my_ref', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('issued_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('letter_url', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('received_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('added_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('entered_user', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('original_excel', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
    ]
