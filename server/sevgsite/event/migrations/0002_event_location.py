# Generated by Django 4.1.1 on 2022-09-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]