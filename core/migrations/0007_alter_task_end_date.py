# Generated by Django 4.0.3 on 2022-04-04 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_task_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.FloatField(blank=True, null=True),
        ),
    ]