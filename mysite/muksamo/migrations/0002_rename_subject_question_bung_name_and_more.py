# Generated by Django 4.1.5 on 2023-01-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muksamo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='subject',
            new_name='Bung_Name',
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]