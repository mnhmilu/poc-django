# Generated by Django 4.2.5 on 2023-09-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_merge_0004_auto_20230907_1032_0009_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='revised_due_dte',
        ),
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateField(),
        ),
    ]