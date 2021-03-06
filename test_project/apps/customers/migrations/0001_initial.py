# Generated by Django 3.2.4 on 2021-06-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_verified', models.BooleanField(default=False)),
                ('phone', models.CharField(max_length=110, unique=True)),
                ('phone_prefix', models.CharField(max_length=10, verbose_name='Country code')),
                ('phone_suffix', models.CharField(max_length=100, verbose_name='National number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
