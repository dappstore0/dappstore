# Generated by Django 2.1.2 on 2018-10-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='dapp',
            name='days_to_go',
            field=models.IntegerField(default=10),
        ),
    ]
