# Generated by Django 3.1.8 on 2022-03-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('subject', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
