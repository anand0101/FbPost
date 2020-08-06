# Generated by Django 3.0.6 on 2020-08-05 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb1', '0024_auto_20200805_1252'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newsdata',
        ),
        migrations.AlterField(
            model_name='imagepost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 16, 50, 51, 386020)),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 16, 50, 51, 391020)),
        ),
        migrations.AlterField(
            model_name='videopost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 16, 50, 51, 389020)),
        ),
    ]