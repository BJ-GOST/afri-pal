# Generated by Django 4.1.4 on 2022-12-16 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0002_rename_amount_job_budget_job_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
