# Generated by Django 3.1.2 on 2020-10-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_auto_20201015_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blogApp.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='teams',
            field=models.ManyToManyField(to='blogApp.Team'),
        ),
    ]
