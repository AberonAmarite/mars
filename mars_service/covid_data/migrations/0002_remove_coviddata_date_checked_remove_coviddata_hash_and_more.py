# Generated by Django 4.2.3 on 2023-08-03 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coviddata',
            name='date_checked',
        ),
        migrations.RemoveField(
            model_name='coviddata',
            name='hash',
        ),
        migrations.RemoveField(
            model_name='coviddata',
            name='last_modified',
        ),
    ]
