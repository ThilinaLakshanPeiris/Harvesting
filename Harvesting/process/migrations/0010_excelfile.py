# Generated by Django 4.1.2 on 2023-07-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0009_alter_forestletter_original_excel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
