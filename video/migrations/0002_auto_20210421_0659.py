# Generated by Django 3.1.2 on 2021-04-20 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='ahem',
            field=models.CharField(default='aa', max_length=255),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='bhem',
            field=models.CharField(default='ba', max_length=255),
        ),
    ]
