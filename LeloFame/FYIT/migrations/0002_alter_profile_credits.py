# Generated by Django 3.2.4 on 2022-01-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYIT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='credits',
            field=models.IntegerField(default=0),
        ),
    ]