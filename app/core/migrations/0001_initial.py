# Generated by Django 3.2.19 on 2023-06-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='First name')),
                ('last_name', models.CharField(max_length=128, verbose_name='Last name')),
                ('birth_place', models.CharField(max_length=128, verbose_name='Birth place')),
            ],
            options={
                'verbose_name': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Jedi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='First name')),
                ('last_name', models.CharField(max_length=128, verbose_name='Last name')),
                ('force', models.IntegerField(verbose_name='Force')),
            ],
            options={
                'verbose_name': 'Jedi',
            },
        ),
    ]
