# Generated by Django 3.0.6 on 2020-07-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagepost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('caption', models.CharField(default=None, max_length=2222)),
                ('image', models.ImageField(default=None, upload_to='profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Videopost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('caption', models.CharField(default=None, max_length=2222)),
                ('utube_video_link', models.CharField(max_length=2222)),
            ],
        ),
    ]
