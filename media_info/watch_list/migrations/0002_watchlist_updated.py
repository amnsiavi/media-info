# Generated by Django 5.0.6 on 2024-05-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
