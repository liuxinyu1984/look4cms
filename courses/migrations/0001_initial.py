# Generated by Django 4.2.3 on 2023-08-11 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(help_text='Year of the term, e.g. 2023', max_length=4, verbose_name='Year')),
                ('season', models.CharField(choices=[('W1', 'Fall'), ('W2', 'Spring'), ('S1', 'Summer_1'), ('S2', 'Summer_2')], help_text='Season of the term, e.g. Fall.', max_length=8, verbose_name='Season')),
                ('start_date', models.DateField(help_text='Start date of the term.', verbose_name='Start Date')),
                ('end_date', models.DateField(help_text='End date of the term.', verbose_name='End Date')),
            ],
        ),
    ]
