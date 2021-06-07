# Generated by Django 3.2.4 on 2021-06-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('actors', models.ManyToManyField(to='crud_api.Actor')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
