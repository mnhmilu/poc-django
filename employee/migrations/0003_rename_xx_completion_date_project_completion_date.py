# Generated by Django 4.2.5 on 2023-10-15 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_completion_date_project_xx_completion_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='xx_completion_date',
            new_name='completion_date',
        ),
    ]
