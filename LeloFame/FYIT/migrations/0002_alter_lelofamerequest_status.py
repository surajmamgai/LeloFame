# Generated by Django 3.2 on 2022-01-31 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYIT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lelofamerequest',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
