# Generated by Django 3.0.8 on 2020-07-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiktactoe_app', '0007_auto_20200706_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='sm_nos',
            field=models.CharField(max_length=100),
        ),
    ]