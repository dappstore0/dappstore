# Generated by Django 2.1.2 on 2018-10-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181027_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('key', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
            ],
        ),
    ]