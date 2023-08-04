# Generated by Django 4.2.3 on 2023-08-03 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('date_checked', models.DateTimeField()),
                ('death', models.IntegerField()),
                ('death_increase', models.IntegerField()),
                ('hash', models.CharField(max_length=255)),
                ('hospitalized', models.IntegerField()),
                ('hospitalized_cumulative', models.IntegerField()),
                ('hospitalized_currently', models.IntegerField()),
                ('hospitalized_increase', models.IntegerField()),
                ('in_icu_cumulative', models.IntegerField()),
                ('in_icu_currently', models.IntegerField()),
                ('last_modified', models.DateTimeField()),
                ('negative', models.IntegerField()),
                ('negative_increase', models.IntegerField()),
                ('on_ventilator_cumulative', models.IntegerField()),
                ('on_ventilator_currently', models.IntegerField()),
                ('pending', models.IntegerField()),
                ('pos_neg', models.IntegerField()),
                ('positive', models.IntegerField()),
                ('positive_increase', models.IntegerField()),
                ('recovered', models.IntegerField(null=True)),
                ('states', models.IntegerField()),
                ('total', models.IntegerField()),
                ('total_test_results', models.IntegerField()),
                ('total_test_results_increase', models.IntegerField()),
            ],
        ),
    ]
