# Generated by Django 4.1.2 on 2022-12-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('breach_num', models.IntegerField(default=0)),
                ('street_address', models.CharField(max_length=100)),
                ('apt_number', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=80)),
                ('state_abbreviation', models.CharField(max_length=2)),
                ('zipcode', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('breach_type', models.CharField(max_length=20)),
                ('breach_description', models.CharField(max_length=1000)),
                ('breach_datetime', models.DateTimeField()),
            ],
        ),
    ]
