# Generated by Django 4.0.1 on 2022-01-27 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYIT', '0005_lelofamelog_delete_creditlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='lelofamerequest',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
