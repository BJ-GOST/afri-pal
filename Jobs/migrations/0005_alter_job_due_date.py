# Generated by Django 4.1.4 on 2022-12-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0004_job_job_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]
