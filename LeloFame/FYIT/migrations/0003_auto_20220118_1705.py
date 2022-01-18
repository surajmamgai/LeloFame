# Generated by Django 3.2.4 on 2022-01-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FYIT', '0002_auto_20220118_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditlog',
            old_name='idd',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='creditlog',
            old_name='userid',
            new_name='userusername',
        ),
        migrations.RenameField(
            model_name='creditpurchaselog',
            old_name='idd',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='lelofamerequest',
            old_name='idd',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='lelofamerequest',
            old_name='userid',
            new_name='userusername',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]