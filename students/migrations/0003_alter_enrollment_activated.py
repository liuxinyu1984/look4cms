# Generated by Django 4.2.4 on 2023-09-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_enrollments_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='activated',
            field=models.BooleanField(default=False, verbose_name='Activated by Administration'),
        ),
    ]
