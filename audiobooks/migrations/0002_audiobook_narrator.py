# Generated by Django 2.1.2 on 2018-12-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiobooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiobook',
            name='narrator',
            field=models.CharField(default='unknown', max_length=200),
        ),
    ]
