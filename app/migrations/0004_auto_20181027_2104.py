# Generated by Django 2.1.2 on 2018-10-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='dapp',
            name='blockchain',
            field=models.CharField(default='ethereum', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dapp',
            name='current_fund',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dapp',
            name='fund_next_stage',
            field=models.IntegerField(default=10),
        ),
    ]