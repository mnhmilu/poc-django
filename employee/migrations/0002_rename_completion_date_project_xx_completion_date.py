# Generated by Django 4.2.5 on 2023-10-15 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='completion_date',
            new_name='xx_completion_date',
        ),
    ]