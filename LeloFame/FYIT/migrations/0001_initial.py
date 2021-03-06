# Generated by Django 3.2 on 2022-02-01 07:15

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('credits', models.IntegerField(default=0)),
                ('reffered_by', models.CharField(default='999999', max_length=300, null=True)),
                ('total_refferal', models.IntegerField(default=0)),
                ('reedemed_refferal', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reffered_to', models.CharField(max_length=200)),
                ('now', models.CharField(max_length=50, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeloFameRequest',
            fields=[
                ('txn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('userhandle', models.CharField(max_length=200)),
                ('platform', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('plan', models.CharField(max_length=300)),
                ('status', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeloFameLog',
            fields=[
                ('txn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('credit_spends', models.IntegerField()),
                ('platform', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('userhandle', models.CharField(max_length=200)),
                ('credit_left', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('plan', models.CharField(max_length=300)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditPurchaseRequest',
            fields=[
                ('txn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('credit', models.IntegerField(default=0)),
                ('amount', models.IntegerField()),
                ('paymentslip', models.FileField(null=True, upload_to='paymentslip/')),
                ('status', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditPurchaseLog',
            fields=[
                ('txn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('credit_previous_balanace', models.IntegerField()),
                ('credit_new_balance', models.IntegerField()),
                ('credit_value', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
